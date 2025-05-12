import os
import pandas as pd

# 定义项目根目录路径
project_root = os.getcwd()  # 假设合并.py位于项目根目录

# 定义需要处理的地区文件夹
regions = ['澳门paper', '台湾digital-bridge', '香港paper']

# 定义需要合并的关键字
target_keywords = ['ASA', 'ASG', 'ASH', 'ACG', 'AST']

# 定义一个函数来合并指定文件夹中的文件
def merge_region_data(region):
    # 构造地区文件夹路径
    region_path = os.path.join(project_root, '港澳台', region)
    
    # 检查文件夹是否存在
    if not os.path.exists(region_path):
        print(f"文件夹 {region_path} 不存在，跳过")
        return
    
    # 获取该地区所有包含目标关键字的xlsx文件
    xlsx_files = [f for f in os.listdir(region_path) if f.endswith('.xlsx') and not f.startswith('~$') and any(keyword in f for keyword in target_keywords)]
    
    # 如果没有符合条件的xlsx文件，跳过
    if not xlsx_files:
        print(f"文件夹 {region_path} 中没有找到符合条件的Excel文件，跳过")
        return
    
    # 读取每个文件的数据
    dataframes = []
    for file_name in xlsx_files:
        file_path = os.path.join(region_path, file_name)
        print(f"正在处理文件: {file_path}")  # 调试信息
        try:
            df = pd.read_excel(file_path, engine='openpyxl')
            dataframes.append(df)
        except Exception as e:
            print(f"读取文件 {file_path} 时出错: {e}")
    
    # 如果没有数据，跳过
    if not dataframes:
        print(f"文件夹 {region_path} 中没有有效数据，跳过")
        return
    
    # 合并所有数据表，按公共列组合关联
    merged_df = dataframes[0]
    for i in range(1, len(dataframes)):
        # 找到两个表中共有的列
        common_columns = merged_df.columns.intersection(dataframes[i].columns)
        if len(common_columns) == 0:
            print(f"文件 {xlsx_files[i]} 与之前的合并结果没有公共列，跳过")
            continue
        # 合并数据
        merged_df = pd.merge(merged_df, dataframes[i], on=list(common_columns), how='outer')
        print(f"已合并文件 {xlsx_files[i]}")

    # 增加 LINK_index 列
    if all(col in merged_df.columns for col in ['IDCNTRY', 'IDSCHOOL', 'IDTEACH', 'IDLINK', 'IDTEALIN', 'IDGRADE']):
        merged_df['LINK_index'] = merged_df['IDCNTRY'].astype(str) + merged_df['IDSCHOOL'].astype(str) + merged_df['IDTEACH'].astype(str) + merged_df['IDLINK'].astype(str) + merged_df['IDTEALIN'].astype(str) + merged_df['IDGRADE'].astype(str)
        print("已增加 LINK_index 列")
    else:
        print("缺少必要的列，无法生成 LINK_index 列")

    
    # 保存合并后的数据到新的 CSV 文件
    output_path = os.path.join(project_root, '港澳台', f"{region}_merged_data.csv")
    merged_df.to_csv(output_path, index=False, encoding='utf-8-sig')
    print(f"合并完成，文件已保存为 {output_path}")

# 遍历每个地区，分别合并数据
for region in regions:
    print(f"开始合并 {region} 的数据")
    merge_region_data(region)
    print(f"{region} 的数据合并完成\n")