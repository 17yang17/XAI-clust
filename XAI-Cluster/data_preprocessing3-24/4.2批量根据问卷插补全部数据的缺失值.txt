import pandas as pd
import os

project_root = os.getcwd()  # 假设合并.py位于项目根目录

# 读取澳门.csv文件
file_path = os.path.join(project_root, '处理完缺失值', 'with_NA_澳门paper_merged_data.csv')
data = pd.read_csv(file_path)

# 检查并删除语言不为Chinese的样例数据
data = data[data['ITLANG_SA'] == 10]
data = data[data['ITLANG_SQ'] == 10]
data = data[data['ITLANG_HQ'] == 10]
data = data[data['ITLANG_CQ'] == 10]
# data = data[data['ITLANG_TQ'] == 10]

# 去除小样本数据，即学生有两个教师的的样例
data = data[data['NTEACH'] == 1]

# 检查并处理数据
#家庭背景
columns_to_update = ['ASBH02B']
for column in columns_to_update:
    data.loc[(data['ASBH02A'] == 1) & (data[column].isna()), column] = 1

columns_to_update = ['ASBH05B']
for column in columns_to_update:
    data.loc[(data['ASBH05AA'] == 2) & (data['ASBH05AB'] == 2) & (data[column].isna()), column] = 1


columns_to_update = ['ASBH20A','ASBH20B','ASBH20C','ASBH21A','ASBH21B','ASBH21C','ASBH21D']
for column in columns_to_update:
    data.loc[(data['ASBH19'] == 2) & (data[column].isna()), column] = 2

columns_to_update = ['ASBH22']
for column in columns_to_update:
    data.loc[(data['ASBH19'] == 2) & (data[column].isna()), column] = 3

# 学校背景
columns_to_update = ['ACBG07B']
for column in columns_to_update:
    data.loc[(data['ACBG07A'] == 2) & (data[column].isna()), column] = 1

columns_to_update = ['ACBG07C']
for column in columns_to_update:
    data.loc[(data['ACBG07A'] == 2) & (data[column].isna()), column] = 2

columns_to_update = ['ACBG21A','ACBG21B','ACBG21C','ACBG21D','ACBG21E','ACBG21F']
for column in columns_to_update:
    data.loc[((data['ACBG20'] == 2) & (data[column].isna())), column] = 2
    data.loc[((data['ACBG20'] == 3) & (data[column].isna())), column] = 2


# 处理异常值
missing_rules = {
    # 家庭背景
    'ASBH17A': [9,99], 
    'ASBH17B': [9,99], 
    'ASBH15A': [99],
    'ASBH15B': [99], 
    }
# print(missing_rules)

# 遍历每个变量，将异常缺失值替换为NA
for variable, missing_values in missing_rules.items():
    if variable in data.columns:
        # 将异常缺失值替换为NA
        data[variable] = data[variable].apply(lambda x: pd.NA if x in missing_values else x)


# 保存修改后的文件
new_file_path = os.path.join(project_root, '根据问卷插补后', '澳门_modified.csv')
data.to_csv(new_file_path, index=False)

print(f"文件已保存为: {new_file_path}")



###################################################################

# 读取台湾.csv文件
file_path = os.path.join(project_root, '处理完缺失值', 'with_NA_台湾digital-bridge_merged_data.csv')
data = pd.read_csv(file_path)


# 检查并删除语言不为Chinese的样例数据
data = data[data['ITLANG_SA'] == 10]
data = data[data['ITLANG_SQ'] == 10]
data = data[data['ITLANG_HQ'] == 10]
data = data[data['ITLANG_CQ'] == 10]
# data = data[data['ITLANG_TQ'] == 10]

# 去除小样本数据，即学生有两个教师的的样例
data = data[data['NTEACH'] == 1]

# 检查并处理数据
#家庭背景
columns_to_update = ['ASBH02B']
for column in columns_to_update:
    data.loc[(data['ASBH02A'] == 1) & (data[column].isna()), column] = 1

columns_to_update = ['ASBH05B']
for column in columns_to_update:
    data.loc[(data['ASBH05AA'] == 2) & (data['ASBH05AB'] == 2) & (data[column].isna()), column] = 1


columns_to_update = ['ASBH20A','ASBH20B','ASBH20C','ASBH21A','ASBH21B','ASBH21C','ASBH21D']
for column in columns_to_update:
    data.loc[(data['ASBH19'] == 2) & (data[column].isna()), column] = 2

columns_to_update = ['ASBH22']
for column in columns_to_update:
    data.loc[(data['ASBH19'] == 2) & (data[column].isna()), column] = 3

# 学校背景
columns_to_update = ['ACBG07B']
for column in columns_to_update:
    data.loc[(data['ACBG07A'] == 2) & (data[column].isna()), column] = 1

columns_to_update = ['ACBG07C']
for column in columns_to_update:
    data.loc[(data['ACBG07A'] == 2) & (data[column].isna()), column] = 2

columns_to_update = ['ACBG21A','ACBG21B','ACBG21C','ACBG21D','ACBG21E','ACBG21F']
for column in columns_to_update:
    data.loc[((data['ACBG20'] == 2) & (data[column].isna())), column] = 2
    data.loc[((data['ACBG20'] == 3) & (data[column].isna())), column] = 2


# 处理异常值
missing_rules = {
    # 家庭背景
    'ASBH17A': [9,99], 
    'ASBH17B': [9,99], 
    'ASBH15A': [99],
    'ASBH15B': [99], 
    }
# print(missing_rules)

# 遍历每个变量，将异常缺失值替换为NA
for variable, missing_values in missing_rules.items():
    if variable in data.columns:
        # 将异常缺失值替换为NA
        data[variable] = data[variable].apply(lambda x: pd.NA if x in missing_values else x)


# 保存修改后的文件
new_file_path = os.path.join(project_root, '根据问卷插补后', '台湾_modified.csv')
data.to_csv(new_file_path, index=False)

print(f"文件已保存为: {new_file_path}")


###################################################################


# 读取香港.csv文件
file_path = os.path.join(project_root, '处理完缺失值', 'with_NA_香港paper_merged_data.csv')
data = pd.read_csv(file_path)


# 检查并删除语言不为Chinese的样例数据
data = data[data['ITLANG_SA'] == 10]
data = data[data['ITLANG_SQ'] == 10]
data = data[data['ITLANG_HQ'] == 10]
data = data[data['ITLANG_CQ'] == 10]
# data = data[data['ITLANG_TQ'] == 10]

# 去除小样本数据，即学生有两个教师的的样例
data = data[data['NTEACH'] == 1]

# 检查并处理数据
#家庭背景
columns_to_update = ['ASBH02B']
for column in columns_to_update:
    data.loc[(data['ASBH02A'] == 1) & (data[column].isna()), column] = 1

columns_to_update = ['ASBH05B']
for column in columns_to_update:
    data.loc[(data['ASBH05AA'] == 2) & (data['ASBH05AB'] == 2) & (data[column].isna()), column] = 1


columns_to_update = ['ASBH20A','ASBH20B','ASBH20C','ASBH21A','ASBH21B','ASBH21C','ASBH21D']
for column in columns_to_update:
    data.loc[(data['ASBH19'] == 2) & (data[column].isna()), column] = 2

columns_to_update = ['ASBH22']
for column in columns_to_update:
    data.loc[(data['ASBH19'] == 2) & (data[column].isna()), column] = 3

# 学校背景
columns_to_update = ['ACBG07B']
for column in columns_to_update:
    data.loc[(data['ACBG07A'] == 2) & (data[column].isna()), column] = 1

columns_to_update = ['ACBG07C']
for column in columns_to_update:
    data.loc[(data['ACBG07A'] == 2) & (data[column].isna()), column] = 2

columns_to_update = ['ACBG21A','ACBG21B','ACBG21C','ACBG21D','ACBG21E','ACBG21F']
for column in columns_to_update:
    data.loc[((data['ACBG20'] == 2) & (data[column].isna())), column] = 2
    data.loc[((data['ACBG20'] == 3) & (data[column].isna())), column] = 2

# 处理异常值
missing_rules = {
    # 家庭背景
    'ASBH17A': [9,99], 
    'ASBH17B': [9,99], 
    'ASBH15A': [99],
    'ASBH15B': [99], 
    }
# print(missing_rules)

# 遍历每个变量，将异常缺失值替换为NA
for variable, missing_values in missing_rules.items():
    if variable in data.columns:
        # 将异常缺失值替换为NA
        data[variable] = data[variable].apply(lambda x: pd.NA if x in missing_values else x)


# 保存修改后的文件
new_file_path = os.path.join(project_root, '根据问卷插补后', '香港_modified.csv')
data.to_csv(new_file_path, index=False)

print(f"文件已保存为: {new_file_path}")

