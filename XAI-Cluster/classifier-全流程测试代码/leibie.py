# import pandas as pd
# import re

# # 读取源数据
# source_file = 'c:/Users/杨洋/WPSDrive/450155367/WPS云盘/P21codebook/P21_Codebook.xlsx'
# source_df = pd.read_excel(source_file, sheet_name='全部变量')

# # 预定义的分类变量列表
# cat_vars = ['ITSEX', 'ASRIBM', 'ASBG03', 'ASBG05A', 'ASBG05B', 'ASBG05E', 'ASBG05F', 'ASBG05G', 'ASBG05H', 'ASBG05I', 'ASBG05J', 'ASBG05K', 'ASBG06', 'ASBG07A', 'ASBG07B', 'ASBG08A', 'ASBG08B', 'ASBG10F', 'ASBR03A', 'ASBR03B', 'ASBR03C', 'ASBR04', 'ASBR05', 'ASDGSEC', 'ASDGSSB', 'ASDGSB', 'ASDGERL', 'ASDGDRL', 'ASDGSLR', 'ASDGSCR', 'ASDG05S', 'ASBH02A', 'ASBH02B', 'ASBH03A', 'ASBH03B', 'ASBH03C', 'ASBH03D', 'ASBH03E', 'ASBH04', 'ASBH06', 'ASBH07F', 'ASBH09', 'ASBH14A', 'ASBH14B', 'ASBH14C', 'ASBH16', 'ASBH18AA', 'ASBH18AB', 'ASBH18BA', 'ASBH18BB', 'ASBH18CA', 'ASBH18CB', 'ASBH18DA', 'ASBH18DB', 'ASBH18EA', 'ASBH18EB', 'ASBH19', 'ASBH20A', 'ASBH20B', 'ASBH20C', 'ASBH21A', 'ASBH21B', 'ASBH21C', 'ASBH21D', 'ASBH22', 'ASDGHRL', 'ASDHSES', 'ASDHELA', 'ASDHENA', 'ASDHELN', 'ASDHELT', 'ASDHPCS', 'ASDHPLR', 'ASDHAPS', 'ASDHEDUP', 'ASDHOCCP', 'ACBG04', 'ACBG05A', 'ACBG05B', 'ACBG07A', 'ACBG07B', 'ACBG07C', 'ACBG08', 'ACBG13', 'ACBG14A', 'ACBG14B', 'ACBG14C', 'ACBG14D', 'ACBG14E', 'ACBG14F', 'ACBG14G', 'ACBG14H', 'ACBG14I', 'ACBG14J', 'ACBG14K', 'ACBG14L', 'ACBG14M', 'ACBG14N', 'ACBG17', 'ACBG18A', 'ACBG18B', 'ACBG18C', 'ACBG19', 'ACBG20', 'ACBG21A', 'ACBG21B', 'ACBG21C', 'ACBG21D', 'ACBG21E', 'ACBG21F', 'ACDGRRS', 'ACDGEAS', 'ACDGDAS', 'ACDGSBC', 'ATBG02', 'ATBG03', 'ATBG05AA', 'ATBG05AB', 'ATBG05AC', 'ATBG05AD', 'ATBG05BA', 'ATBG05BB', 'ATBG05BC', 'ATBG05BD', 'ATBG05BE', 'ATBG05BF', 'ATBG05BG', 'ATBG05BH', 'ATBG05BI', 'ATBG05BJ', 'ATBG05BK', 'ATBG06', 'ATBG07AA', 'ATBG07BA', 'ATBG07AB', 'ATBG07BB', 'ATBG07AC', 'ATBG07BC', 'ATBG07AD', 'ATBG07BD', 'ATBG07AE', 'ATBG07BE', 'ATBG07AF', 'ATBG07BF', 'ATBG07AG', 'ATBG07BG', 'ATBG08A', 'ATBG08B', 'ATBG08C', 'ATBG08D', 'ATBG08E', 'ATBG09A', 'ATBG09B', 'ATBG09C', 'ATBG09D', 'ATBR06A', 'ATBR06B', 'ATBR06C', 'ATBR06D', 'ATBR06E', 'ATBR07AA', 'ATBR07AB', 'ATBR07AC', 'ATBR07AD', 'ATBR07BA', 'ATBR07BB', 'ATBR07BC', 'ATBR07BD', 'ATBR08A', 'ATBR08B', 'ATBR08C', 'ATBR08D', 'ATBR08E', 'ATBR08F', 'ATBR08G', 'ATBR08H', 'ATBR09A', 'ATBR09B', 'ATBR09C', 'ATBR09D', 'ATBR09E', 'ATBR09F', 'ATBR09G', 'ATBR09H', 'ATBR09I', 'ATBR10A', 'ATBR10B', 'ATBR10C', 'ATBR10D', 'ATBR10E', 'ATBR10F', 'ATBR10G', 'ATBR10H', 'ATBR10I', 'ATBR10J', 'ATBR10K', 'ATBR10L', 'ATBR11A', 'ATBR11B', 'ATBR11C', 'ATBR11D', 'ATBR11E', 'ATBR12A', 'ATBR12BA', 'ATBR12BB', 'ATBR12BC', 'ATBR12BD', 'ATBR12C', 'ATBR12DA', 'ATBR12DB', 'ATBR12DC', 'ATBR12EA', 'ATBR12EB', 'ATBR12EC', 'ATBR12ED', 'ATBR12EE', 'ATBR13A', 'ATBR13B', 'ATBR13C', 'ATBR13D', 'ATBR13E', 'ATBR14', 'ATBR15', 'ATBR16', 'ATBR17A', 'ATBR17B', 'ATBR17C', 'ATBR18A', 'ATBR18B', 'ATBR18C', 'ATBR18D', 'ATBR18E', 'ATBR19', 'ATDGEAS', 'ATDGSOS', 'ATDGTJS', 'ATDGSLI']

# # ------------------------- 修改开始 -------------------------
# # 根据 cat_vars 动态生成目标DataFrame
# target_df = pd.DataFrame(columns=['变量名', '类别', '类别解释'])

# # 遍历分类变量列表
# for var_name in cat_vars:
#     # 在源数据中查找变量定义
#     var_data = source_df[source_df['变量'] == var_name]
    
#     if not var_data.empty:
#         # 提取详细值方案
#         detail_explanation = var_data.iloc[0]['详细值方案']
        
#         # 解析类别定义
#         if pd.notna(detail_explanation):
#             matches = re.findall(r'(\d+):([^;]*)', str(detail_explanation))
#             for match in matches:
#                 category = match[0].strip()
#                 # 追加到目标DataFrame
#                 target_df = pd.concat([
#                     target_df,
#                     pd.DataFrame([[var_name, category, '']], 
#                                 columns=['变量名', '类别', '类别解释'])
#                 ], ignore_index=True)
# # ------------------------- 修改结束 -------------------------

# # 创建详细值解释字典
# detail_dict = {}
# for index, row in source_df.iterrows():
#     variable_name = row['变量']
#     detail_explanation = row['详细值方案']
    
#     if pd.notna(detail_explanation):
#         matches = re.findall(r'(\d+):([^;]*)', str(detail_explanation))
#         for match in matches:
#             category = match[0].strip()
#             explanation = match[1].strip()
#             detail_dict[(variable_name, category)] = explanation

# # 填充类别解释
# for index, row in target_df.iterrows():
#     variable_name = row['变量名']
#     category = str(row['类别'])
#     key = (variable_name, category)
    
#     if key in detail_dict:
#         target_df.at[index, '类别解释'] = detail_dict[key]

# # 保存结果（可选）
# output_file = 'd:/XAI/XAI-Cluster/classifier/实验变量选择_自动生成.xlsx'
# target_df.to_excel(output_file, index=False, sheet_name='分类变量解释')

# print(f"生成的分类变量解释已保存到: {output_file}")






import pandas as pd
import re

# 读取源数据和目标数据
source_file = 'c:/Users/杨洋/WPSDrive/450155367/WPS云盘/P21codebook/P21_Codebook.xlsx'  # 源文件名
target_file = 'C:/Users/杨洋/WPSDrive/450155367/WPS云盘/毕设论文/变量选择.xlsx'      # 目标文件名

# 读取源表格和目标表格
source_df = pd.read_excel(source_file, sheet_name='全部变量')
target_df = pd.read_excel(target_file, sheet_name='分类')

# 创建一个字典来存储详细值解释
detail_dict = {}

# 遍历源表格，解析详细值解释
for index, row in source_df.iterrows():
    variable_name = row['变量']
    detail_explanation = row['详细值方案']
    
    # 确保 detail_explanation 是字符串类型
    if not isinstance(detail_explanation, str):
        detail_explanation = str(detail_explanation)
    
    # 使用正则表达式提取类别和解释
    matches = re.findall(r'(\d+):([^;]*)', detail_explanation)
    for match in matches:
        category = match[0].strip()
        explanation = match[1].strip()
        detail_dict[(variable_name, category)] = explanation

# 遍历目标表格，填充类别解释
for index, row in target_df.iterrows():
    variable_name = row['变量名']
    category = str(row['类别'])
    key = (variable_name, category)
    
    # 如果找到匹配的详细值解释，则填充到目标表格
    if key in detail_dict:
        target_df.at[index, '类别解释'] = detail_dict[key]


# 保存结果（可选）
output_file = 'd:/XAI/XAI-Cluster/classifier/实验变量选择_自动生成.xlsx'
target_df.to_excel(output_file, index=False, sheet_name='分类变量解释')

print(f"生成的分类变量解释已保存到: {output_file}")