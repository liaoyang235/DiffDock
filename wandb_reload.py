import pandas as pd
import wandb

# 读取CSV文件
file_path = 'wandb_export.csv'  # 替换为你的CSV文件路径
df = pd.read_csv(file_path)

# 指定要读取的两列
column1 = 'DTR_0.6_wo_for_eval - train_loss'  # 替换为第一列的列名

# 去除所有NaN值
df1 = df[column1].dropna()


# 初始化wandb
wandb.init(project="diffdock", name="upload_combined_column")

# 将拼接结果上传至wandb
for index, value in enumerate(df1):
    wandb.log({"train_loss": value},step=index+1)

# 结束wandb运行
wandb.finish()
