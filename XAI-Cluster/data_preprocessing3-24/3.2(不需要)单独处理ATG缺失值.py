import os
import pandas as pd

# 读取缺失值规则表
missing_rules_df = pd.read_excel('P21codebook/P21_Codebook.xlsx',sheet_name='ATGR5')  # 如果是 Excel 文件，使用 pd.read_excel

# 定义一个函数来解析缺失值规则
def parse_missing_values(rule_str):
    # 如果规则字符串为空，返回空列表
    if pd.isna(rule_str) or rule_str.strip() == '':
        return []
    
    # 按分号分隔不同的规则
    rules = rule_str.split(';')
    missing_values = []
    
    for rule in rules:
        # 每条规则的格式为 "值: 描述"
        parts = rule.strip().split(':', 1)  # 只分割一次，避免描述中包含冒号影响结果
        if len(parts) == 2:
            value_str = parts[0].strip()
            # 尝试将值转换为整数，如果失败则忽略
            try:
                value = int(value_str)
                missing_values.append(value)
            except ValueError:
                pass
    
    return missing_values

# 将缺失值规则表转换为字典
missing_rules = {}
for _, row in missing_rules_df.iterrows():
    variable = row['Variable']
    rule_str = row['Missing Scheme Detailed: R']
    missing_values = parse_missing_values(rule_str)
    if missing_values:
        missing_rules[variable] = missing_values


# 定义项目根目录路径
project_root = os.getcwd()  # 假设合并.py位于项目根目录
input_path = os.path.join(project_root, '港澳台')
# 读取ATG文件
atg_df = pd.read_csv(os.path.join(input_path, 'ATG.csv'))

# print(missing_rules)

# 遍历每个变量，将缺失值替换为NA
for variable, missing_values in missing_rules.items():
    if variable in atg_df.columns:
        # 将缺失值替换为NA
        atg_df[variable] = atg_df[variable].apply(lambda x: pd.NA if x in missing_values else x)

# 保存处理后的数据
atg_df.to_csv(os.path.join(input_path, 'ATG_with_NA.csv'), index=False)
print("ATG文件处理完成，已保存为ATG_with_NA.csv")