# 加载必要的包
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

# 确认文件是否正确加载
if (length(rdata_files) == 0) {
  stop("没有找到任何 .RData 文件，请检查文件夹路径或文件格式")
}

# 循环处理每个 .RData 文件
for (rdata_file in rdata_files) {
  # 加载 .RData 文件
  load(rdata_file)
  # print(rdata_file)
  # 获取加载的对象名称
  objects <- ls()
  
  # 获取文件名（不包括扩展名）
  file_base_name <- tools::file_path_sans_ext(basename(rdata_file))
  
  # 设置一个标志，确保每个文件只导出第一个符合条件的对象
  #exported <- FALSE
  
  # 遍历对象，将数据框对象保存为 .xlsx 文件
  for (obj_name in objects) {
    # print(obj_name)
    
    obj <- get(obj_name)
    
    # # 检查对象是否为数据框
    if (is.data.frame(obj) && file_base_name == obj_name) {
    
      # 创建输出文件路径，使用原文件名加上对象名
      output_file <- file.path(output_folder, paste0(basename(rdata_file), "_", obj_name, ".xlsx"))
      
      # print(basename(rdata_file))
      
      # 导出数据框为 .xlsx 文件
      write_xlsx(obj, output_file)
      message("已导出：", output_file)
      
      # 设置标志，标识已经导出过一个对象
      #exported <- TRUE
    }
  }
 
  
  # 清理环境中的对象，准备处理下一个文件
  # rm(list = objects)
}
