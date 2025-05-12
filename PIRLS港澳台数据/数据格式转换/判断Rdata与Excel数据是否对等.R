# install.packages("writexl")

library(writexl)  # 用于导出为 Excel 文件

# 指定包含 .RData 文件的文件夹路径和输出路径
input_folder <- "F:/P21_Data_R/Data"  # 替换为你的 .RData 文件夹路径
output_folder <- "F:/P21_Data_R/Excel"  # 替换为保存 Excel 文件的输出路径

# 创建输出文件夹（如果不存在）
if (!dir.exists(output_folder)) {
  dir.create(output_folder, showWarnings = FALSE)
}

# 获取 .RData 文件列表
rdata_files <- list.files(input_folder, pattern = "\\.Rdata$", full.names = TRUE)

print(length(rdata_files))
  
# 获取 .xlsx文件列表
rdata_files2 <- list.files(output_folder, pattern = "\\.xlsx$", full.names = TRUE)

print(length(rdata_files2))
  
  