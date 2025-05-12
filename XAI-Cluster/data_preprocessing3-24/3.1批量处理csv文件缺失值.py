import pandas as pd
import os

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

# 定义一个函数来处理单个工作表
def process_sheet(df):
    missing_rules = {}
    for _, row in df.iterrows():
        variable = row['Variable']
        rule_str = row['Missing Scheme Detailed: R']
        missing_values = parse_missing_values(rule_str)
        if missing_values:
            missing_rules[variable] = missing_values
    return missing_rules

# 定义一个函数来处理单个文件
def process_file(file_path):
    # 读取 Excel 文件中的所有工作表
    excel_file = pd.ExcelFile(file_path)
    all_sheets = excel_file.sheet_names
    total_rules = {}
    
    for sheet_name in all_sheets:
        # 读取单个工作表
        df = excel_file.parse(sheet_name)
        # 处理工作表并获取规则
        sheet_rules = process_sheet(df)
        # 合并到总规则中
        total_rules.update(sheet_rules)
    
    return total_rules

# 定义一个函数来处理文件夹中的所有文件
def process_folder(folder_path):
    total_missing_rules = {}
    
    # 遍历文件夹中的所有文件
    for file_name in os.listdir(folder_path):
        # 检查文件是否是 Excel 文件
        if file_name.endswith('.xlsx'):
            file_path = os.path.join(folder_path, file_name)
            # 处理单个文件并获取规则
            file_rules = process_file(file_path)
            # 合并到总规则中
            total_missing_rules.update(file_rules)
    
    return total_missing_rules

# 定义项目根目录路径
project_root = os.getcwd()  # 假设合并.py位于项目根目录

# 构造港澳台文件夹路径
region_path = os.path.join(project_root, 'P21codebook')

# 生成总的缺失值规则字典
total_missing_rules = process_folder(region_path)

# # 打印总的缺失值规则字典
# print(total_missing_rules)

# 定义项目根目录路径
project_root = os.getcwd()  # 假设合并.py位于项目根目录

# 构造待处理文件夹路径
data_folder = os.path.join(project_root, '港澳台')  # 假设CSV文件在港澳台文件夹中

# 定义一个函数来处理单个CSV文件
def process_csv_file(file_path, missing_rules):
    # 读取CSV文件
    df = pd.read_csv(file_path)
    
    # 遍历每个变量，将缺失值替换为NA
    for variable, missing_values in missing_rules.items():
        if variable in df.columns:
            # 将缺失值替换为NA
            df[variable] = df[variable].apply(lambda x: pd.NA if x in missing_values else x)
    
    return df

# 定义一个函数来批量处理文件夹中的所有CSV文件
def batch_process_csv_files(folder_path, missing_rules):
    # 遍历文件夹中的所有文件
    for file_name in os.listdir(folder_path):
        # 检查文件是否是CSV文件
        if file_name.endswith('.csv'):
            file_path = os.path.join(folder_path, file_name)
            # 处理单个CSV文件
            processed_df = process_csv_file(file_path, missing_rules)
            # 保存处理后的文件
            processed_file_path = os.path.join(project_root, '处理完缺失值', f"with_NA_{file_name}")
            processed_df.to_csv(processed_file_path, index=False)
            print(f"处理完成: {file_name} -> {processed_file_path}")

# 批量处理文件夹中的CSV文件
batch_process_csv_files(data_folder, total_missing_rules)
