import torch.nn as nn
import numpy as np
import torch



# TODO: Change argument names with alpha and beta
def create_mask_tasks(task_count, unit_count, beta, init_method, alpha=4):
    if init_method == "DTR":
        _unit_mapping = torch.zeros((task_count, unit_count))
        num_filled_channel = int(unit_count * beta)
        last_index = unit_count - num_filled_channel
        index = ((np.linspace(0, 1, task_count) ** alpha) * last_index).round().astype(np.int64)
        for task in range(task_count):
            _unit_mapping[task, index[task] : index[task] + num_filled_channel] = torch.ones((num_filled_channel))
    elif init_method == "random":
        _unit_mapping = torch.zeros((task_count, unit_count))
        num_filled_channel = int(unit_count * beta)
        _unit_mapping[np.arange(task_count)[:, None], np.random.rand(task_count, unit_count).argsort(1)[:, :num_filled_channel]] = 1
    else:
        raise ValueError(f"unsupported init method: {init_method}")
    return _unit_mapping


class TaskRouter(nn.Module):

    """
    Same as https://github.com/gstrezoski/TaskRouting/blob/master/taskrouting.py
    Applies task specific masking out individual units in a layer.

    Args:
    unit_count  (int): Number of input channels going into the Task Routing layer.
    task_count  (int): Number of tasks. (IN STL it applies to number of output classes)
    sigma (int): Ratio for routed units per task.
    """

    def __init__(self, unit_count, task_count, sigma, init_method, alpha):
        super(TaskRouter, self).__init__()

        self.unit_count = unit_count
        # Just initilize it with 0. This gets changed right after the model is loaded so the value is never used.
        # We store the active mask for the Task Routing Layer here.
        self.active_task = 0
        self.task_count = task_count


        #！！！！！！！事先创建好所有的mask
        _unit_mapping = create_mask_tasks(
            task_count,
            unit_count,
            beta=sigma,
            init_method=init_method,
            alpha = alpha
        )
        self.register_buffer("_unit_mapping", _unit_mapping)

    def set_active_task(self, active_task):

        #！！！！！！！根据目前的task步数，从_unit_mapping中选择对应的mask
        self.active_task = active_task
        dev = active_task.device

        #！！！！！！！ (torch.ones(len(active_task), device=active_task.device) * self.active_task)的形状是1*N，每一个task的序号
        self.active_mask = torch.index_select(self._unit_mapping.to(dev), 0, (torch.ones(len(active_task), device=active_task.device) * self.active_task).long()).unsqueeze(1)
        return active_task

    def forward(self, input, module_input):
        input = module_input + input * (1 - self.active_mask)
        return input
    
if __name__ == "__main__":
    task_router = TaskRouter(20, 100, 0.6, "DTR", 0.25)
    task_router.set_active_task(torch.tensor([i for i in range(100)]))
    active_mask = task_router.active_mask
    import matplotlib.pyplot as plt

    # Visualize the active_mask
    plt.imshow(active_mask.squeeze().cpu().numpy(), aspect='auto', cmap='viridis')
    plt.colorbar(label='Mask Value')
    plt.xlabel('Units')
    plt.ylabel('Tasks')
    plt.title('Active Mask Visualization')
    plt.show()
