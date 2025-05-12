
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
from sklearn.cluster import KMeans, AgglomerativeClustering

# Set the seed
# 设置种子
np.random.seed(42)

# Numerical and categorical variable lists
# 数值和分类变量列表
num_vars = ["ATBG01","ATBR01A","ATBR01B","ATBR02A","ATBR02B","ATBR04",
            "ATBR05","ATBGEAS","ATBGSOS","ATBGTJS","ATBGSLI","ATDGLIHY","ATDGRIHY"]

cat_vars = ["ITLANG_TQ","LCID_TQ","ATBG02","ATBG03","ATBG04",
            "ATBG05AA","ATBG05AB","ATBG05AC","ATBG05AD","ATBG05BA","ATBG05BB",
            "ATBG05BC","ATBG05BD","ATBG05BE","ATBG05BF","ATBG05BG","ATBG05BH",
            "ATBG05BI","ATBG05BJ","ATBG05BK","ATBG06","ATBG07AA","ATBG07BA",
            "ATBG07AB","ATBG07BB","ATBG07AC","ATBG07BC","ATBG07AD","ATBG07BD",
            "ATBG07AE","ATBG07BE","ATBG07AF","ATBG07BF","ATBG07AG","ATBG07BG",
            "ATBG08A","ATBG08B","ATBG08C","ATBG08D","ATBG08E","ATBG09A","ATBG09B",
            "ATBG09C","ATBG09D","ATBG10A","ATBG10B","ATBG10C","ATBG10D","ATBG10E",
            "ATBG10F","ATBG10G","ATBG10H","ATBG10I","ATBG10J","ATBG10K","ATBG10L",
            "ATBG11A","ATBG11B","ATBG11C","ATBG11D","ATBG11E","ATBG11F","ATBG11G",
            "ATBG11H","ATBG11I","ATBG12A","ATBG12B","ATBG12C","ATBG12D","ATBG12E",
            "ATBG12F","ATBR03A","ATBR03B","ATBR03C","ATBR03D","ATBR03E","ATBR03F",
            "ATBR03G","ATBR03H","ATBR06A","ATBR06B","ATBR06C","ATBR06D","ATBR06E",
            "ATBR07AA","ATBR07AB","ATBR07AC","ATBR07AD","ATBR07BA","ATBR07BB",
            "ATBR07BC","ATBR07BD","ATBR08A","ATBR08B","ATBR08C","ATBR08D","ATBR08E",
            "ATBR08F","ATBR08G","ATBR08H","ATBR09A","ATBR09B","ATBR09C","ATBR09D",
            "ATBR09E","ATBR09F","ATBR09G","ATBR09H","ATBR09I","ATBR10A","ATBR10B",
            "ATBR10C","ATBR10D","ATBR10E","ATBR10F","ATBR10G","ATBR10H","ATBR10I",
            "ATBR10J","ATBR10K","ATBR10L","ATBR11A","ATBR11B","ATBR11C","ATBR11D",
            "ATBR11E","ATBR12A","ATBR12BA","ATBR12BB","ATBR12BC","ATBR12BD","ATBR12C",
            "ATBR12DA","ATBR12DB","ATBR12DC","ATBR12EA","ATBR12EB","ATBR12EC",
            "ATBR12ED","ATBR12EE","ATBR13A","ATBR13B","ATBR13C","ATBR13D","ATBR13E",
            "ATBR14","ATBR15","ATBR16","ATBR17A","ATBR17B","ATBR17C","ATBR18A","ATBR18B",
            "ATBR18C","ATBR18D","ATBR18E","ATBR19","ATDGEAS","ATDGSOS","ATDGTJS","ATDGSLI"]

# 打印数值变量和分类变量
print('数值变量:', len(num_vars))
print('分类变量:', len(cat_vars))

# Load data # 加载数据
df = pd.read_csv('data/ATG_modified.csv')
columns_to_extract = ["LINK_index","ITLANG_TQ","LCID_TQ","ATBG01","ATBG02","ATBG03","ATBG04",
                    "ATBG05AA","ATBG05AB","ATBG05AC","ATBG05AD","ATBG05BA","ATBG05BB","ATBG05BC","ATBG05BD",
                    "ATBG05BE","ATBG05BF","ATBG05BG","ATBG05BH","ATBG05BI","ATBG05BJ","ATBG05BK","ATBG06",
                    "ATBG07AA","ATBG07BA","ATBG07AB","ATBG07BB","ATBG07AC","ATBG07BC","ATBG07AD","ATBG07BD",
                    "ATBG07AE","ATBG07BE","ATBG07AF","ATBG07BF","ATBG07AG","ATBG07BG","ATBG08A","ATBG08B",
                    "ATBG08C","ATBG08D","ATBG08E","ATBG09A","ATBG09B","ATBG09C","ATBG09D","ATBG10A","ATBG10B",
                    "ATBG10C","ATBG10D","ATBG10E","ATBG10F","ATBG10G","ATBG10H","ATBG10I","ATBG10J","ATBG10K",
                    "ATBG10L","ATBG11A","ATBG11B","ATBG11C","ATBG11D","ATBG11E","ATBG11F","ATBG11G","ATBG11H",
                    "ATBG11I","ATBG12A","ATBG12B","ATBG12C","ATBG12D","ATBG12E","ATBG12F","ATBR01A","ATBR01B",
                    "ATBR02A","ATBR02B","ATBR03A","ATBR03B","ATBR03C","ATBR03D","ATBR03E","ATBR03F","ATBR03G",
                    "ATBR03H","ATBR04","ATBR05","ATBR06A","ATBR06B","ATBR06C","ATBR06D","ATBR06E","ATBR07AA",
                    "ATBR07AB","ATBR07AC","ATBR07AD","ATBR07BA","ATBR07BB","ATBR07BC","ATBR07BD","ATBR08A",
                    "ATBR08B","ATBR08C","ATBR08D","ATBR08E","ATBR08F","ATBR08G","ATBR08H","ATBR09A","ATBR09B",
                    "ATBR09C","ATBR09D","ATBR09E","ATBR09F","ATBR09G","ATBR09H","ATBR09I","ATBR10A","ATBR10B",
                    "ATBR10C","ATBR10D","ATBR10E","ATBR10F","ATBR10G","ATBR10H","ATBR10I","ATBR10J","ATBR10K",
                    "ATBR10L","ATBR11A","ATBR11B","ATBR11C","ATBR11D","ATBR11E","ATBR12A","ATBR12BA","ATBR12BB",
                    "ATBR12BC","ATBR12BD","ATBR12C","ATBR12DA","ATBR12DB","ATBR12DC","ATBR12EA","ATBR12EB",
                    "ATBR12EC","ATBR12ED","ATBR12EE","ATBR13A","ATBR13B","ATBR13C","ATBR13D","ATBR13E","ATBR14",
                    "ATBR15","ATBR16","ATBR17A","ATBR17B","ATBR17C","ATBR18A","ATBR18B","ATBR18C","ATBR18D",
                    "ATBR18E","ATBR19","ATBGEAS","ATDGEAS","ATBGSOS","ATDGSOS","ATBGTJS","ATDGTJS","ATBGSLI",
                    "ATDGSLI","ATDGLIHY","ATDGRIHY"]
# 提取指定的列，组成新的 DataFrame
df = df[columns_to_extract]

# 移除方差为零的数值变量
num_vars_filtered = [var for var in num_vars if df[var].var() > 0]
# 更新 num_vars 并筛选 DataFrame
num_vars = num_vars_filtered  # 确保后续步骤使用过滤后的变量列表

# 移除分类变量中唯一值总数小于2的分类变量 和 方差为零的分类变量
cat_vars_filtered = [var for var in cat_vars if df[var].nunique() >= 2 and df[var].var() > 0]
# 添加额外检查：删除唯一值数量为1的变量
cat_vars_filtered = [var for var in cat_vars_filtered if df[var].nunique() > 1]
# 更新 num_vars 并筛选 DataFrame
cat_vars = cat_vars_filtered  # 确保后续步骤使用过滤后的变量列表
# print(df[cat_vars].nunique())

# 打印数值变量和分类变量
print('数值变量:', len(num_vars), num_vars)
print('分类变量:', len(cat_vars), cat_vars)

# 提取指定的列，组成新的 DataFrame
columns_to_extract = ["LINK_index"] + num_vars + cat_vars
df = df[columns_to_extract]

# print(df)
# 数据预处理 DATA PREPROCESSING
print('--- 数据预处理 DATA PREPROCESSING ---')
from clearn.data_preprocessing import *

# 原始数据样本数
print(f"原始数据样本数: {len(df)}")

# 计算缺失值 Computre missing values
n_missing = df.isnull().sum().sum()
print('缺失值 Missing values:', n_missing, f'({n_missing*100/df.size}%)')
# 打印缺失值统计 Compute missing values
print("打印缺失值统计:\n", compute_missing(df))

# 生成缺失值热图 Generate missing values heat map
missing_values_heatmap(df, output_path=os.path.join("img", "缺失值热图missing_heatmap.jpg"))

# print('数值变量类型:', df[num_vars].dtypes)
# print('分类变量类型:', df[cat_vars].dtypes)

# 插补缺失值 Impute missing values
df_imp = impute_missing_values(df, num_vars=num_vars, cat_vars=cat_vars)

print(f"插补缺失值后剩余样本数: {len(df_imp)}")

# 打印数值变量和分类变量
print('数值变量:', len(num_vars))
print('分类变量:', len(cat_vars))
# plot_imputation_distribution_assessment(df.loc[df_imp.index], df_imp, list(compute_missing(df).head(16)['var_name']))

# 绘制插补前后所选变量分布之间的比较
# Plot the comparison between the distribution of a selection of variables before and after imputation
plot_imputation_distribution_assessment(df.loc[df_imp.index], df_imp, list(compute_missing(df).head(16)['var_name']),
                                        output_path=os.path.join("img", "插补分布对比图imputation_distribution_assessment.jpg"))

# 删除异常值 Remove outliers
# df_, outliers = remove_outliers(df_imp, num_vars+cat_vars)

# 删除异常值 Remove outliers，调整参数以匹配论文结果
# 删除异常值 Remove outliers（调整参数以匹配论文结果）
# iForest_kws = { # 论文中删除315个样本（4556-4241）
#     'max_samples': 0.7,
#     'max_features': 0.7,
#     'bootstrap': False,
#     'random_state': 42  # 确保可重复性
# }

# 异常值检测
df_, outliers = remove_outliers(df_imp, num_vars + cat_vars, iforest_kws=None)
print(f"删除异常值后剩余样本数: {len(df_)}")
# df_ = df

# 在降维代码前添加检查
print("分类变量唯一值总和:", df_[cat_vars].nunique().sum())

# 降维 DIMENSIONALITY REDUCTION
print('--- 降维 DIMENSIONALITY REDUCTION ---')
df_ = df_.reset_index(drop=True)  # 重置索引
# 插补结果保存
df_.to_csv('data/ATG_data_preprocessing.csv', index=False)
# 连接列表 x 和 y
z = num_vars + cat_vars

from clearn.dimensionality_reduction import DimensionalityReduction
# 实例化类，并将其投影到最优成分数量的低维空间
# Instantiate class, project to a lower dimensionality with optimal number of components
dr = DimensionalityReduction(df_[z], num_vars=num_vars, cat_vars=cat_vars, num_algorithm='spca')
df_t = dr.transform(min_explained_variance_ratio=None)

print("降维后的全部变量数量：", dr.n_components_, "降维后的数值变量数量：", len(dr.num_components_), "降维后的分类变量的数量：", len(dr.cat_components_))
print("降维后的数值变量：", dr.num_components_)
print("降维后的分类变量：", dr.cat_components_)

# # 过滤掉方差为 0 的数值变量
# num_vars_filtered = [var for var in dr.num_components_ if df_t[var].var() > 0]
# print("过滤后的数值变量：", num_vars_filtered)

# # 过滤掉方差为 0 的分类变量
# cat_vars_filtered = [var for var in dr.cat_components_ if df_t[var].var() > 0]
# print("过滤后的分类变量：", cat_vars_filtered)



# 解释第四个提取成分 Explain fourth extracted component
print("打印主要贡献变量:\n", dr.num_main_contributors(dim_idx=3)) # 打印主要贡献变量 # 可以根据需要修改参数
# 绘制主要贡献变量图表
dr.plot_num_main_contributors(dim_idx=3, output_path=os.path.join("img", "主要贡献变量图表dim_red_main_contributors.jpg"))

# 解释从分类变量中提取的成分
# Explain component extracted from categorical variables
print("解释从分类变量中提取的成分:\n", dr.cat_main_contributors_stats())
# 在分类变量的降维过程中（如MCA）后，有65个原始变量与新的构造变量（主成分）高度相关，默认相关性阈值为0.14
# 绘制分类变量成分分布
dr.plot_cat_main_contributor_distribution(dim_idx=0, 
                                          thres=0.2,  # 提高相关性阈值
                                          n_contributors=10,  # 增加显示数量
                                          output_path=os.path.join("img", "分类变量成分分布dim_red_cat_component.jpg"))

# 解释方差 + 肘部法 Explained variance + elbow method
dr.plot_num_explained_variance(0.5, plots=['cumulative', 'normalized'],
                               output_path=os.path.join("img", "dim_red_explained_variance.jpg"))

# 聚类 CLUSTERING
print('--- 聚类 CLUSTERING ---')
from clearn.clustering import Clustering

# 实例化类并在投影空间计算聚类
# Instantiate class and compute clusters on projected space
# cl = Clustering(df_t, algorithms=['KMeans()', 'AgglomerativeClustering()'], normalize=False)
# 实例化类并在投影空间计算聚类
cl = Clustering(
    df_t, 
    algorithms=[KMeans(random_state=42), AgglomerativeClustering()],  # 传入算法实例
    normalize=False
)
cl.compute_clusters(max_clusters=21, prefix='TEA')
print(cl.optimal_config_)

# 绘制每个聚类的观测数  # 聚类结果可视化
# Plot number of observations per cluster
cl.plot_clustercount(output_path=os.path.join("img", "聚类数量分布图cluster_count.jpg"))

# 绘制用于选择最优 k 的标准化 WSS 曲线  # 最优聚类数选择曲线
# Plot normalized WSS curve for optimal k selection
cl.plot_optimal_components_normalized(output_path=os.path.join("img", "最优聚类数选择曲线clustering_elbow_curve.jpg"))

# 比较聚类内均值与全局均值 # 聚类均值对比热图
# Compare intra-cluster means to global means
print(cl.compare_cluster_means_to_global_means())
cl.plot_cluster_means_to_global_means_comparison(xlabel='Principal Components', ylabel='Clusters',
                                                 levels=[-1, -0.67, -0.3, -0.15, 0.15, 0.3, 0.67, 1],
                                                 output_path=os.path.join("img", "聚类均值对比热图clustering_intra_comparison.jpg"))

# 比较原始变量在各聚类中的分布
# Compare distributions of original variables by cluster
cl.plot_distribution_comparison_by_cluster(df_ext=df_[['ATBGEAS', 'ATBGTJS']],
                                           output_path=os.path.join("img", "clustering_distribution_comparison.jpg"))

# 2-D plots # 二维图
cl.plot_clusters_2D('dim_01', 'dim_02', output_path=os.path.join("img", "clustering_2d_plots.jpg"))

# 比较原始分类变量在各聚类中的分布
# Comparison of original categorical variable distribution by cluster
print(cl.describe_clusters_cat(df_['ATDGRIHY'], cat_name='ATDGRIHY', normalize=True))
cl.plot_cat_distribution_by_cluster(df_['ATDGRIHY'], cat_label='ATDGRIHY', cluster_label='Teacher clusters',
                                    output_path=os.path.join("img", "原始分类变量在各聚类中的分布clustering_cat_comparison.jpg"))

# 将聚类分配给包含原始变量的数据框
# Assign clusters to data frame with original variables
df_['cluster'] = cl.df['cluster'].values
df_['cluster_cat'] = cl.df['cluster_cat'].values

# print(list(df_.columns()))

# 删除TEA_04这个类别
# df_ = df_[df_['cluster'] != 4]

# CLASSIFIER # 分类器
print('--- CLASSIFIER 分类---')
from clearn.classifier import Classifier
np.random.seed(42)

# 用原始变量实例化类。将上面计算的聚类设置为目标
# Instantiate the class with the original variables. As target, we set the clusters computed above
var_list = list(df_.columns[1:-2])  # 除了第一个和最后两个列
print(var_list)

print(df_['cluster'].value_counts())

classifier = Classifier(df_, predictor_cols=var_list, target=df_['cluster'], num_cols=num_vars, cat_cols=cat_vars)

# Build a pipeline with feature selection, hyperparameter tuning, and model fitting. For feature selection, we make sure
# that variable ESCS (economic, social and cultural status) gets selected (features_to_keep=['ESCS']). Hyperparameter
# optimization is performed through exhaustive grid search for different values of the number of estimators
# (n_estimators=[30, 60]), eta (eta=[0.15, 0.25]), and maximum tree depth (max_depth=[3, 5, 7]). The algorithms used are
# those configured by default, i.e. random forest for feature selection and xgboost for the final classification model.
# 构建一个包含特征选择、超参数调整和模型拟合的管道。
# 在特征选择中，确保变量 ESCS（经济、社会和文化地位）被选中（features_to_keep=['ESCS']）。
# 通过穷举网格搜索对估计器数量（n_estimators=[30, 60]）、eta（eta=[0.15, 0.25]）和最大树深度（max_depth=[3, 5, 7]）的不同值进行超参数优化。
# 使用的算法是默认配置的，即随机森林用于特征选择，xgboost 用于最终分类模型。
classifier.train_model(features_to_keep=['ATBGEAS', 'ATDGEAS','ATBGSOS', 'ATDGSOS','ATBGTJS','ATDGTJS', 'ATBGSLI', 'ATDGSLI','ATDGLIHY', 'ATDGRIHY'], 
                       hyperparameter_tuning=True,
                       param_grid=dict(n_estimators=[30, 60], eta=[0.15, 0.25], max_depth=[5, 7, 9])# 确保传递类别数
                       )

# 获取五个最重要特征的全局特征重要性 打印特征重要性
# Get global feature importance of the five most important features
print("前五个最重要特征的全局特征重要性:\n", classifier.feature_importances.head())

# 绘制全局特征重要性图
# Plot global feature importance
classifier.plot_shap_importances(output_path=os.path.join("img", "全局特征重要性图classifier_global_feature_importance.jpg"))
plt.clf()

# 绘制标识符为 1 和 2 的聚类的局部重要性
# Plot local importance for clusters with identifiers 1 and 2
classifier.plot_shap_importances_beeswarm(class_id=1,
                                          output_path=os.path.join("img", "标识符1聚类的局部重要性classifier_local_importance_cl1.jpg"))
plt.clf()
classifier.plot_shap_importances_beeswarm(class_id=2,
                                          output_path=os.path.join("img", "标识符2聚类的局部重要性classifier_local_importance_cl2.jpg"))
plt.clf()

# Performance assessment # 性能评估  # 模型评估输出（开始）
# Hyperparameter tuning results # 超参数调整结果
print("超参数调优结果:\n", classifier.hyperparameter_tuning_metrics()) # 打印超参数调优结果

# Confusion matrix # 混淆矩阵 # 绘制混淆矩阵
classifier.plot_confusion_matrix(output_path=os.path.join("img", "混淆矩阵classifier_confusion_matrix.jpg"))

# Classification report # # 打印分类报告
print("分类报告:\n", classifier.classification_report())

# ROC curves # ROC 曲线
classifier.plot_roc_curves(output_path=os.path.join("img", "ROC曲线classifier_roc_curves.jpg"))







