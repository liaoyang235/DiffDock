import os 
import pandas as pd
import argparse

parser = argparse.ArgumentParser(description='Generate CSV for protein-ligand pairs')

# path should be one of the followings:
# DockGen/processed_files
# posebusters_paper_data/astex_diverse_set
# posebusters_paper_data/posebusters_diverse_set

parser.add_argument('--path', type=str, default='DockGen/processed_files')
parser.add_argument('--out', type=str, default='test_dockgen.csv', help='output csv file name')
parser.add_argument('--multiple', action='store_true', default=False, help='decide whether use multiple ligands in posebusters')
args = parser.parse_args()

folder_path = args.path
if 'DockGen' in folder_path:
    pairs = []
    for folder in os.listdir(folder_path):
        if not os.path.isdir(os.path.join(folder_path, folder)):
            continue
        protein = ''
        ligand=[]
        for file in os.listdir(os.path.join(folder_path, folder)):
            if os.path.isdir(os.path.join(folder_path, folder, file)):
                continue
            path = os.path.join(folder_path, folder, file)
            if file[0] == '.':
                continue
            postfix = file.split('_')[-1]
            if postfix == 'ligand.pdb':
                ligand.append(path)
            elif postfix == 'processed.pdb':
                protein = path
        for lig in ligand:
            pairs.append([folder,protein,lig,''])

if 'posebusters' or 'astex' in folder_path:
    pairs = []

    for folder in os.listdir(folder_path):
        if not os.path.isdir(os.path.join(folder_path, folder)):
            continue
        protein = ''
        ligand=[]
        for file in os.listdir(os.path.join(folder_path, folder)):
            if os.path.isdir(os.path.join(folder_path, folder, file)):
                continue
            path = os.path.join(folder_path, folder, file)
            postfix = file.split('_')[-1]
            if postfix == 'ligands.sdf' and args.multiple:
                ligand.append(path)
            elif postfix == 'ligand.sdf' and not args.multiple:
                ligand.append(path)
            elif postfix == 'protein.pdb':
                protein = path
        for lig in ligand:
            pairs.append([folder,protein,lig,''])


df = pd.DataFrame(pairs, columns=['complex_name', 'protein_path', 'ligand_description', 'protein_sequence'])
df.to_csv(args.out, index=False)