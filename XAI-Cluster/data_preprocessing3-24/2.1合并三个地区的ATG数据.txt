import os
import pandas as pd

# 定义项目根目录路径
project_root = os.getcwd()  # 假设合并.py位于项目根目录

# 定义需要处理的地区文件夹
regions = ['澳门paper', '台湾digital-bridge', '香港paper']

# 定义需要合并的关键字和对应的输出文件名
merge_keywords = {
    # 'AST': 'AST.csv',
    'ATG': 'ATG.csv'
}

# 遍历每个关键字
for keyword, output_file in merge_keywords.items():
    # 用于存储所有符合条件的 DataFrame
    all_data = pd.DataFrame()
    
    # 遍历每个地区文件夹
    for region in regions:
        # 构造港澳台文件夹路径
        region_path = os.path.join(project_root, '港澳台', region)
        # 检查文件夹是否存在
        if os.path.exists(region_path):
            # 遍历地区文件夹中的所有文件
            for file_name in os.listdir(region_path):
                # 检查文件名是否包含关键字，并且是 Excel 文件
                if keyword in file_name and file_name.endswith('.xlsx'):
                    file_path = os.path.join(region_path, file_name)
                    print(f"正在处理文件: {file_path}")  # 调试信息
                    # 检查文件是否存在
                    if os.path.exists(file_path):
                        try:
                            # 读取 Excel 文件，指定引擎为 openpyxl
                            df = pd.read_excel(file_path, engine='openpyxl')
                            # 将数据添加到 all_data
                            all_data = pd.concat([all_data, df], ignore_index=True)
                        except Exception as e:
                            print(f"读取文件 {file_path} 时出错: {e}")
                    else:
                        print(f"文件 {file_path} 不存在，跳过")
        else:
            print(f"文件夹 {region_path} 不存在，跳过")
    
    # 如果有数据，则保存为 CSV 文件
    if not all_data.empty:

        # 增加 LINK_index 列
        if all(col in all_data.columns for col in ['IDCNTRY', 'IDSCHOOL', 'IDTEACH', 'IDLINK', 'IDTEALIN', 'IDGRADE']):
            all_data['LINK_index'] = all_data['IDCNTRY'].astype(str) + all_data['IDSCHOOL'].astype(str) + all_data['IDTEACH'].astype(str) + all_data['IDLINK'].astype(str) + all_data['IDTEALIN'].astype(str) + all_data['IDGRADE'].astype(str)
            print("已增加 LINK_index 列")
        else:
            print("缺少必要的列，无法生成 LINK_index 列")

        output_path = os.path.join(project_root, '港澳台', output_file)
        all_data.to_csv(output_path, index=False, encoding='utf-8-sig')
        print(f"成功合并 {keyword} 文件，保存为 {output_path}")
    else:
        print(f"没有找到 {keyword} 的文件，跳过合并")