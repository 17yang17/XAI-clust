import os
import pandas as pd
from functools import reduce

# 加载 CSV 文件
project_root = os.getcwd()  # 假设脚本位于项目根目录
file_path = os.path.join(project_root, "pre")

# 指定文件路径列表
file_paths = [
    "data_澳门_modified_preprocess_ouput.csv",
    "data_台湾_modified_preprocess_ouput.csv",
    "data_香港_modified_preprocess_ouput.csv",
]

# 读取所有.csv文件的完整路径
file_paths_all = [os.path.join(file_path, file) for file in file_paths]

# ================== 数值变量处理部分 ==================
# 初始化存储所有地区数值结果的列表
numeric_dfs = []

def process_numeric(file_path, region_name):
    """处理单个文件的数值变量"""
    df = pd.read_csv(file_path)
    
    # 创建地区专属的列名
    results = pd.DataFrame(columns=['Variable', 
                                  f'Mean_{region_name}', 
                                  f'Std_{region_name}'])
    
    # 筛选数值型变量（根据实际类型调整）
    numeric_cols = df.select_dtypes(include=['float64']).columns
    
    for col in numeric_cols:
        new_row = pd.DataFrame({
            'Variable': [col],
            f'Mean_{region_name}': [df[col].mean()],
            f'Std_{region_name}': [df[col].std()]
        })
        results = pd.concat([results, new_row], ignore_index=True)
    
    return results

# 处理所有文件
region_names = ["澳门", "台湾", "香港"]
for idx, path in enumerate(file_paths_all):
    numeric_df = process_numeric(path, region_names[idx])
    numeric_dfs.append(numeric_df)

# 合并所有地区结果
final_numeric = reduce(
    lambda left,right: pd.merge(left, right, on='Variable', how='outer'),
    numeric_dfs
)

# 保存最终结果
numeric_output_path = os.path.join(file_path, 'combined_numeric_stats.csv')
final_numeric.to_csv(numeric_output_path, index=False)
print(f"数值统计合并文件已保存至: {numeric_output_path}")



import os
import pandas as pd

# 加载 CSV 文件
project_root = os.getcwd()  # 假设脚本位于项目根目录
file_path = os.path.join(project_root, "pre")

# 指定文件路径列表
file_paths = [
    "data_澳门_modified_preprocess_ouput.csv",
    "data_台湾_modified_preprocess_ouput.csv",
    "data_香港_modified_preprocess_ouput.csv",
]

# 读取所有.csv文件的完整路径
file_paths_all = [os.path.join(file_path, file) for file in file_paths]

# 定义一个函数来处理每个文件并返回分类变量的频数统计
def process_file(file_path):
    # 读取 CSV 文件
    df = pd.read_csv(file_path)
    
    # 创建一个字典来存储分类变量的频数统计
    categorical_stats = {}
    
    # 遍历 DataFrame 的每一列
    for column in df.columns:
        # 判断是否为分类变量（int64）
        if df[column].dtype == 'int64':
            # 计算每个类别的频数
            category_counts = df[column].value_counts()
            for category, count in category_counts.items():
                # 将结果存储在字典中
                key = (column, category)
                categorical_stats[key] = count
    
    return categorical_stats

# 处理每个文件并收集统计信息
all_stats = {}
region_names = ["澳门", "台湾", "香港"]
for idx, path in enumerate(file_paths_all):
    region_stats = process_file(path)
    all_stats[region_names[idx]] = region_stats

# 收集所有分类变量和编码组合
all_keys = set()
for region_stats in all_stats.values():
    all_keys.update(region_stats.keys())

# 将所有统计信息整合到一个 DataFrame 中
columns = ['变量名', '编码', '澳门样本频数（f）', '台湾样本频数（f）', '香港样本频数（f）']
final_df = pd.DataFrame(columns=columns)

# 遍历所有分类变量和编码，填充 DataFrame
for var, cat in all_keys:
    row = {
        '变量名': var,
        '编码': cat,
        '澳门样本频数（f）': all_stats[region_names[0]].get((var, cat), 0),
        '台湾样本频数（f）': all_stats[region_names[1]].get((var, cat), 0),
        '香港样本频数（f）': all_stats[region_names[2]].get((var, cat), 0)
    }
    final_df = pd.concat([final_df, pd.DataFrame([row])], ignore_index=True)

# 保存最终结果到 CSV 文件
output_file = os.path.join(file_path, 'combined_categorical_statistics.csv')
final_df.to_csv(output_file, index=False)
print(f"合并后的分类变量统计结果已保存到: {output_file}")