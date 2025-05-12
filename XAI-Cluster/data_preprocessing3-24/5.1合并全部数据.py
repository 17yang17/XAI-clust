import os
import pandas as pd

project_root = os.getcwd()  # 假设合并.py位于项目根目录
file_path = os.path.join(project_root, "根据问卷插补后")
# print(file_path)

# 指定文件路径列表
file_paths = [
    "澳门_modified.csv",
    "台湾_modified.csv",
    "香港_modified.csv",
    "ATG_modified.csv"
]

# 读取.csv文件路径
file_paths_all = []
for file in file_paths:
    file_paths_all.append(os.path.join(file_path, file))

print(file_paths_all)

# 读取每个文件的数据
dataframes = [pd.read_csv(file) for file in file_paths_all]

# 合并所有数据表，按 识别变量Identification Variables 组合关联
# ['IDCNTRY', 'IDSCHOOL', 'IDCLASS', 'IDSTUD', 'IDTEACH', 'IDLINK', 'IDTEALIN', 'IDGRADE', 'IDBOOK']

asa_df = dataframes[0]
# 找到两个表中共有的列
common_columns = dataframes[0].columns.intersection(dataframes[3].columns)
print(list(common_columns))
MAC_df = pd.merge(dataframes[0], dataframes[3], on=list(common_columns), how='left')

# 单独处理ATG数据
# 检查并删除语言不为Chinese的样例数据
MAC_df = MAC_df[MAC_df['ITLANG_TQ'] == 10]
# 去除小样本数据，即学生有两个教师的的样例
MAC_df = MAC_df[MAC_df['LINK_index'] != 34451405140011514001014]
MAC_df = MAC_df[MAC_df['LINK_index'] != 34451405140022514002024]
# 去除空白数据
MAC_df = MAC_df[MAC_df['LINK_index'] != 44650425042025504202054]


# 计算平均“总体阅读”得分
MAC_df['ASRREA'] = MAC_df[['ASRREA01', 'ASRREA02', 'ASRREA03', 'ASRREA04', 'ASRREA05']].mean(axis=1, skipna=True)

# 计算平均“文学目的”得分
MAC_df['ASRLIT'] = MAC_df[['ASRLIT01', 'ASRLIT02', 'ASRLIT03', 'ASRLIT04', 'ASRLIT05']].mean(axis=1, skipna=True)

# 计算平均“信息性目的”得分
MAC_df['ASRINF'] = MAC_df[['ASRINF01', 'ASRINF02', 'ASRINF03', 'ASRINF04', 'ASRINF05']].mean(axis=1, skipna=True)

# 计算平均“解释过程”得分
MAC_df['ASRIIE'] = MAC_df[['ASRIIE01', 'ASRIIE02', 'ASRIIE03', 'ASRIIE04', 'ASRIIE05']].mean(axis=1, skipna=True)

# 计算平均“直接过程”得分
MAC_df['ASRRSI'] = MAC_df[['ASRRSI01', 'ASRRSI02', 'ASRRSI03', 'ASRRSI04', 'ASRRSI05']].mean(axis=1, skipna=True)

# 计算平均“国际阅读量表基准达成”等级
MAC_df['ASRIBM_mean'] = MAC_df[['ASRIBM01', 'ASRIBM02', 'ASRIBM03', 'ASRIBM04', 'ASRIBM05']].mean(axis=1, skipna=True)

# 定义一个函数来根据平均“总体阅读”得分计算评级
def calculate_rating(score):
    if score < 400:
        return 1
    elif 400 <= score < 475:
        return 2
    elif 475 <= score < 550:
        return 3
    elif 550 <= score < 625:
        return 4
    else:
        return 5

# 计算平均“总体阅读”得分的评级
MAC_df['ASRREA_rating'] = MAC_df['ASRREA'].apply(calculate_rating)

# 比较平均“总体阅读”得分的评级和ASRIBM_mean的四舍五入取整值，取较大的那个
MAC_df['ASRIBM'] = MAC_df.apply(
    lambda row: round(max(row['ASRREA_rating'], row['ASRIBM_mean'])),
    axis=1
)


# 保存合并后的数据到新的 CSV 文件
output_path = os.path.join(file_path, f"data_{file_paths[0]}")
MAC_df.to_csv(output_path, index=False, encoding='utf-8-sig')
print(f"合并完成，文件已保存为 {output_path}")


asa_df = dataframes[1]
# 找到两个表中共有的列
common_columns = dataframes[1].columns.intersection(dataframes[3].columns)
print(list(common_columns))
TWN_df = pd.merge(dataframes[1], dataframes[3], on=list(common_columns), how='left')

# 单独处理ATG数据
# 检查并删除语言不为Chinese的样例数据
TWN_df = TWN_df[TWN_df['ITLANG_TQ'] == 10]
# 去除小样本数据，即学生有两个教师的的样例
TWN_df = TWN_df[TWN_df['LINK_index'] != 34451405140011514001014]
TWN_df = TWN_df[TWN_df['LINK_index'] != 34451405140022514002024]
# 去除空白数据
TWN_df = TWN_df[TWN_df['LINK_index'] != 44650425042025504202054]

# 计算平均“总体阅读”得分
TWN_df['ASRREA'] = TWN_df[['ASRREA01', 'ASRREA02', 'ASRREA03', 'ASRREA04', 'ASRREA05']].mean(axis=1, skipna=True)

# 计算平均“文学目的”得分
TWN_df['ASRLIT'] = TWN_df[['ASRLIT01', 'ASRLIT02', 'ASRLIT03', 'ASRLIT04', 'ASRLIT05']].mean(axis=1, skipna=True)

# 计算平均“信息性目的”得分
TWN_df['ASRINF'] = TWN_df[['ASRINF01', 'ASRINF02', 'ASRINF03', 'ASRINF04', 'ASRINF05']].mean(axis=1, skipna=True)

# 计算平均“解释过程”得分
TWN_df['ASRIIE'] = TWN_df[['ASRIIE01', 'ASRIIE02', 'ASRIIE03', 'ASRIIE04', 'ASRIIE05']].mean(axis=1, skipna=True)

# 计算平均“直接过程”得分
TWN_df['ASRRSI'] = TWN_df[['ASRRSI01', 'ASRRSI02', 'ASRRSI03', 'ASRRSI04', 'ASRRSI05']].mean(axis=1, skipna=True)

# 计算平均“国际阅读量表基准达成”等级
TWN_df['ASRIBM_mean'] = TWN_df[['ASRIBM01', 'ASRIBM02', 'ASRIBM03', 'ASRIBM04', 'ASRIBM05']].mean(axis=1, skipna=True)

# 定义一个函数来根据平均“总体阅读”得分计算评级
def calculate_rating(score):
    if score < 400:
        return 1
    elif 400 <= score < 475:
        return 2
    elif 475 <= score < 550:
        return 3
    elif 550 <= score < 625:
        return 4
    else:
        return 5

# 计算平均“总体阅读”得分的评级
TWN_df['ASRREA_rating'] = TWN_df['ASRREA'].apply(calculate_rating)

# 比较平均“总体阅读”得分的评级和ASRIBM_mean的四舍五入取整值，取较大的那个
TWN_df['ASRIBM'] = TWN_df.apply(
    lambda row: round(max(row['ASRREA_rating'], row['ASRIBM_mean'])),
    axis=1
)

# 保存合并后的数据到新的 CSV 文件
output_path = os.path.join(file_path, f"data_{file_paths[1]}")
TWN_df.to_csv(output_path, index=False, encoding='utf-8-sig')
print(f"合并完成，文件已保存为 {output_path}")


asa_df = dataframes[2]
# 找到两个表中共有的列
common_columns = dataframes[2].columns.intersection(dataframes[3].columns)
print(list(common_columns))
HKG_df = pd.merge(dataframes[2], dataframes[3], on=list(common_columns), how='left')

# 单独处理ATG数据
# 检查并删除语言不为Chinese的样例数据
HKG_df = HKG_df[HKG_df['ITLANG_TQ'] == 10]
# 去除小样本数据，即学生有两个教师的的样例
HKG_df = HKG_df[HKG_df['LINK_index'] != 34451405140011514001014]
HKG_df = HKG_df[HKG_df['LINK_index'] != 34451405140022514002024]
# 去除空白数据
HKG_df = HKG_df[HKG_df['LINK_index'] != 44650425042025504202054]

# 计算平均“总体阅读”得分
HKG_df['ASRREA'] = HKG_df[['ASRREA01', 'ASRREA02', 'ASRREA03', 'ASRREA04', 'ASRREA05']].mean(axis=1, skipna=True)

# 计算平均“文学目的”得分
HKG_df['ASRLIT'] = HKG_df[['ASRLIT01', 'ASRLIT02', 'ASRLIT03', 'ASRLIT04', 'ASRLIT05']].mean(axis=1, skipna=True)

# 计算平均“信息性目的”得分
HKG_df['ASRINF'] = HKG_df[['ASRINF01', 'ASRINF02', 'ASRINF03', 'ASRINF04', 'ASRINF05']].mean(axis=1, skipna=True)

# 计算平均“解释过程”得分
HKG_df['ASRIIE'] = HKG_df[['ASRIIE01', 'ASRIIE02', 'ASRIIE03', 'ASRIIE04', 'ASRIIE05']].mean(axis=1, skipna=True)

# 计算平均“直接过程”得分
HKG_df['ASRRSI'] = HKG_df[['ASRRSI01', 'ASRRSI02', 'ASRRSI03', 'ASRRSI04', 'ASRRSI05']].mean(axis=1, skipna=True)

# 计算平均“国际阅读量表基准达成”等级
HKG_df['ASRIBM_mean'] = HKG_df[['ASRIBM01', 'ASRIBM02', 'ASRIBM03', 'ASRIBM04', 'ASRIBM05']].mean(axis=1, skipna=True)

# 定义一个函数来根据平均“总体阅读”得分计算评级
def calculate_rating(score):
    if score < 400:
        return 1
    elif 400 <= score < 475:
        return 2
    elif 475 <= score < 550:
        return 3
    elif 550 <= score < 625:
        return 4
    else:
        return 5

# 计算平均“总体阅读”得分的评级
HKG_df['ASRREA_rating'] = HKG_df['ASRREA'].apply(calculate_rating)

# 比较平均“总体阅读”得分的评级和ASRIBM_mean的四舍五入取整值，取较大的那个
HKG_df['ASRIBM'] = HKG_df.apply(
    lambda row: round(max(row['ASRREA_rating'], row['ASRIBM_mean'])),
    axis=1
)

# 保存合并后的数据到新的 CSV 文件
output_path = os.path.join(file_path, f"data_{file_paths[2]}")
HKG_df.to_csv(output_path, index=False, encoding='utf-8-sig')
print(f"合并完成，文件已保存为 {output_path}")





