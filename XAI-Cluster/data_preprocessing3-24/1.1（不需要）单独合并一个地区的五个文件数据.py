import pandas as pd

# 指定文件路径列表
file_paths = [
    "香港paper/ASAHKGR5.Rdata_ASAHKGR5.xlsx",
    "香港paper/ASGHKGR5.Rdata_ASGHKGR5.xlsx",
    "香港paper/ASHHKGR5.Rdata_ASHHKGR5.xlsx",
    "香港paper/ACGHKGR5.Rdata_ACGHKGR5.xlsx",
    "香港paper/ASTHKGR5.Rdata_ASTHKGR5.xlsx",
    "香港paper/ATGHKGR5.Rdata_ATGHKGR5.xlsx"
]

# 读取每个文件的数据
dataframes = [pd.read_excel(file) for file in file_paths]

# 合并所有数据表，按 识别变量Identification Variables 组合关联
# ['IDCNTRY', 'IDSCHOOL', 'IDCLASS', 'IDSTUD', 'IDTEACH', 'IDLINK', 'IDTEALIN', 'IDGRADE', 'IDBOOK']

asa_df = dataframes[0]
# 找到两个表中共有的列
common_columns = dataframes[0].columns.intersection(dataframes[1].columns)
print(list(common_columns))
ASAASG_df = pd.merge(dataframes[0], dataframes[1], on=list(common_columns), how='outer')

# 找到两个表中共有的列
common_columns = ASAASG_df.columns.intersection(dataframes[2].columns)
ASAASGASH_df = pd.merge(ASAASG_df, dataframes[2], on=list(common_columns), how='outer')

# 保存合并后的数据到新的 Excel 文件
ASAASGASH_df.to_csv("ASAASGASH_data.csv", index=False)
print("合并完成，文件已保存为 'ASAASGASH_data.csv'")

# 找到两个表中共有的列
common_columns = ASAASGASH_df.columns.intersection(dataframes[3].columns)
ASAASGASHACG_df = pd.merge(ASAASGASH_df, dataframes[3], on=list(common_columns), how='outer')

# 保存合并后的数据到新的 Excel 文件
ASAASGASHACG_df.to_excel("ASAASGASHACG_data.xlsx", index=False)
print("合并完成，文件已保存为 'ASAASGASHACG_data.xlsx'")

# 找到两个表中共有的列
common_columns = ASAASGASHACG_df.columns.intersection(dataframes[4].columns)
ASAASGASHACGAST_df = pd.merge(ASAASGASHACG_df, dataframes[4], on=list(common_columns), how='outer')

# 保存合并后的数据到新的 Excel 文件
ASAASGASHACGAST_df.to_excel("ASAASGASHACGAST_data.xlsx", index=False)
print("合并完成，文件已保存为 'ASAASGASHACGAST_data.xlsx'")


