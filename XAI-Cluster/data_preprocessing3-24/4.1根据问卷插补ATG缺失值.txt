import pandas as pd
import os

project_root = os.getcwd()  # 假设合并.py位于项目根目录

# 读取ATG.csv文件
file_path = os.path.join(project_root, '处理完缺失值', 'with_NA_ATG.csv')
data = pd.read_csv(file_path)



# 检查并处理数据
columns_to_update = ['ATBR12BA', 'ATBR12BB', 'ATBR12BC', 'ATBR12BD']
for column in columns_to_update:
    data.loc[(data['ATBR12A'] == 2) & (data[column].isna()), column] = 2

columns_to_update = ['ATBR12DA', 'ATBR12DB', 'ATBR12DC']
for column in columns_to_update:
    data.loc[(data['ATBR12A'] == 2) & (data[column].isna()), column] = 3

columns_to_update = ['ATBR12C','ATBR12EA', 'ATBR12EB', 'ATBR12EC', 'ATBR12ED', 'ATBR12EE']
for column in columns_to_update:
    data.loc[(data['ATBR12A'] == 2) & (data[column].isna()), column] = 4

# data.loc[(data['ATBR12A'] == 2) & (data['ATBR12C'].isna()), 'ATBR12C'] = 4

columns_to_update = ['ATBR13B', 'ATBR13C']
for column in columns_to_update:
    data.loc[(data['ATBR13A'] == 2) & (data[column].isna()), column] = 1

columns_to_update = ['ATBR13E']
for column in columns_to_update:
    data.loc[(data['ATBR13A'] == 2) & (data[column].isna()), column] = 2

columns_to_update = ['ATBR13D']
for column in columns_to_update:
    data.loc[(data['ATBR13A'] == 2) & (data[column].isna()), column] = 4

columns_to_update = ['ATBR16']
for column in columns_to_update:
    data.loc[(data['ATBR15'] == 1) & (data[column].isna()), column] = 1

columns_to_update = ['ATBR17A','ATBR17B','ATBR17C']
for column in columns_to_update:
    data.loc[(data['ATBR15'] == 1) & (data[column].isna()), column] = 3
    

# 检查并删除语言不为Chinese的样例数据
data = data[data['ITLANG_TQ'] == 10]

# 去除小样本数据，即学生有两个教师的的样例
data = data[data['LINK_index'] != 34451405140011514001014]
data = data[data['LINK_index'] != 34451405140022514002024]

# 去除空白数据
data = data[data['LINK_index'] != 44650425042025504202054]




# 保存修改后的文件
new_file_path = os.path.join(project_root, '根据问卷插补后', 'ATG_modified.csv')
data.to_csv(new_file_path, index=False)

print(f"文件已保存为: {new_file_path}")