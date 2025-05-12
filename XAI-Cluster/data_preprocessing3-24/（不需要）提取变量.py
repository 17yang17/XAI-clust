import pandas as pd

# 读取 Excel 文件
df = pd.read_excel('stuhomesch_data.xlsx')

# 提取特定列
selected_columns = df[['IDCNTRY', 'IDPOP', 'IDGRADER', 'IDGRADE', 'WAVE', 'IDSCHOOL', 'IDCLASS', 'IDSTUD', 'ITSEX', 'ITADMINI', 'ITLANG_SA', 'LCID_SA', 'IDBOOK', 'ASDAGE', 'HOUWGT', 'TOTWGT', 'SENWGT', 'WGTADJ1', 'WGTADJ2', 'WGTADJ3', 'WGTFAC1', 'WGTFAC2', 'WGTFAC3', 'JKREP', 'JKZONE', 'ASRREA01', 'ASRREA02', 'ASRREA03', 'ASRREA04', 'ASRREA05', 'ASRLIT01', 'ASRLIT02', 'ASRLIT03', 'ASRLIT04', 'ASRLIT05', 'ASRINF01', 'ASRINF02', 'ASRINF03', 'ASRINF04', 'ASRINF05', 'ASRIIE01', 'ASRIIE02', 'ASRIIE03', 'ASRIIE04', 'ASRIIE05', 'ASRRSI01', 'ASRRSI02', 'ASRRSI03', 'ASRRSI04', 'ASRRSI05', 'ASRIBM01', 'ASRIBM02', 'ASRIBM03', 'ASRIBM04', 'ASRIBM05', 'VERSION', 'SCOPE']]

# 保存提取的列到新的 Excel 文件
selected_columns.to_excel('stuhomesch_selected_data.xlsx', index=False)
print("提取的列已保存到 'stuhomesch_selected_data.xlsx'")