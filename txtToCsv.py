import pandas as pd

# 读取.txt文件
txt_file = 'D:/HuangXiaoFang/Projects/task_diversity_BFL-master/data/celeba/Anno/list_eval_partition.txt'
df = pd.read_csv(txt_file, sep=' ', header=None, names=['name', 'partition'])

# 保存为.csv文件
csv_file = 'D:/HuangXiaoFang/Projects/task_diversity_BFL-master/data/celeba/Anno/list_eval_partition.csv'
df.to_csv(csv_file, index=False)