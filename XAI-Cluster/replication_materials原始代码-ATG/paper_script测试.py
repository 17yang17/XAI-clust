# This script contains the code used for the illustration example
# 本脚本包含用于说明示例的代码
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
num_vars = ['AGE', 'PAREDINT', 'BMMJ1',
            'BFMJ2', 'HISEI', 'DURECEC', 'BSMJ', 'MMINS',
            'LMINS', 'SMINS', 'TMINS', 'FCFMLRTY', 'SCCHANGE', 'CHANGE', 'STUBMI',
            'ESCS', 'UNDREM', 'METASUM', 'METASPAM', 'ICTHOME', 'ICTSCH', 'HOMEPOS',
            'CULTPOSS', 'HEDRES', 'WEALTH', 'ICTRES', 'DISCLIMA', 'TEACHSUP',
            'DIRINS', 'PERFEED', 'EMOSUPS', 'STIMREAD', 'ADAPTIVITY', 'TEACHINT',
            'JOYREAD', 'SCREADCOMP', 'SCREADDIFF', 'PERCOMP', 'PERCOOP', 'ATTLNACT',
            'COMPETE', 'WORKMAST', 'GFOFAIL', 'EUDMO', 'SWBP', 'RESILIENCE',
            'MASTGOAL', 'GCSELFEFF', 'GCAWARE', 'ATTIMM', 'INTCULT', 'PERSPECT',
            'COGFLEX', 'RESPECT', 'AWACOM', 'GLOBMIND', 'DISCRIM', 'BELONG',
            'BEINGBULLIED', 'ENTUSE', 'HOMESCH', 'USESCH', 'INTICT', 'COMPICT',
            'AUTICT', 'SOIAICT', 'ICTCLASS', 'ICTOUTSIDE', 'INFOCAR', 'INFOJOB1',
            'INFOJOB2', 'FLCONFIN', 'FLCONICT', 'FLSCHOOL', 'FLFAMILY', 'BODYIMA',
            'SOCONPA']
cat_vars = ['ST004D01T', 'IMMIG', 'REPEAT']



# Load data # 加载数据
df = pd.read_csv('data2/pisa_spain_sample_v2.csv')

# print(df)
# 数据预处理 DATA PREPROCESSING
print('--- 数据预处理 DATA PREPROCESSING ---')
from clearn.data_preprocessing import *

# 原始数据样本数
print(f"原始数据样本数: {len(df)}")

# 计算缺失值 Computre missing values
n_missing = df.isnull().sum().sum()
print('缺失值 Missing values:', n_missing, f'({n_missing*100/df.size}%)')

# 生成缺失值热图 Generate missing values heat map
missing_values_heatmap(df, output_path=os.path.join("img2", "missing_heatmap.jpg"))

print('数值变量类型:', df[num_vars].dtypes)
print('分类变量类型:', df[cat_vars].dtypes)

# 插补缺失值 Impute missing values
df_imp = impute_missing_values(df, num_vars=num_vars, cat_vars=cat_vars)

print(f"插补缺失值后剩余样本数: {len(df_imp)}")

# 绘制插补前后所选变量分布之间的比较
# Plot the comparison between the distribution of a selection of variables before and after imputation
plot_imputation_distribution_assessment(df.loc[df_imp.index], df_imp, ['COMPICT', 'BODYIMA', 'PERCOOP', 'SOCONPA'],
                                        output_path=os.path.join("img2", "imputation_distribution_assessment.jpg"))

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
df_, outliers = remove_outliers(df_imp, num_vars + cat_vars, iforest_kws=None)

print(f"删除异常值后剩余样本数: {len(df_)}")

# 降维 DIMENSIONALITY REDUCTION
print('--- 降维 DIMENSIONALITY REDUCTION ---')
df_ = df_.reset_index(drop=True)
from clearn.dimensionality_reduction import DimensionalityReduction

# 实例化类，并将其投影到最优成分数量的低维空间
# Instantiate class, project to a lower dimensionality with optimal number of components
dr = DimensionalityReduction(df_, num_vars=num_vars, cat_vars=cat_vars, num_algorithm='spca')
df_t = dr.transform(min_explained_variance_ratio=None)
print(dr.n_components_, len(dr.num_components_), len(dr.cat_components_))
print("数值变量：", dr.num_components_, "分类变量：", dr.cat_components_)

# 解释第四个提取成分 Explain fourth extracted component
print(dr.num_main_contributors(dim_idx=3))
dr.plot_num_main_contributors(dim_idx=3, output_path=os.path.join("img2", "dim_red_main_contributors.jpg"))

# 解释从分类变量中提取的成分
# Explain component extracted from categorical variables
print(dr.cat_main_contributors_stats())
dr.plot_cat_main_contributor_distribution(dim_idx=0, output_path=os.path.join("img2", "dim_red_cat_component.jpg"))

# 解释方差 + 肘部法 Explained variance + elbow method
dr.plot_num_explained_variance(0.5, plots=['cumulative', 'normalized'],
                               output_path=os.path.join("img2", "dim_red_explained_variance.jpg"))

# 聚类 CLUSTERING
print('--- 聚类 CLUSTERING ---')
from clearn.clustering import Clustering

# 实例化类并在投影空间计算聚类
# Instantiate class and compute clusters on projected space
# cl = Clustering(df_t, algorithms=['kmeans', 'ward'], normalize=False)
# cl = Clustering(df_t, algorithms=['KMeans()', 'AgglomerativeClustering()'], normalize=False)
# 实例化类并在投影空间计算聚类
cl = Clustering(
    df_t, 
    algorithms=[KMeans(random_state=42), AgglomerativeClustering()],  # 传入算法实例
    normalize=False
)
cl.compute_clusters(max_clusters=21, prefix='STU')
print(cl.optimal_config_)

# 绘制每个聚类的观测数
# Plot number of observations per cluster
cl.plot_clustercount(output_path=os.path.join("img2", "cluster_count.jpg"))

# 绘制用于选择最优 k 的标准化 WSS 曲线
# Plot normalized WSS curve for optimal k selection
cl.plot_optimal_components_normalized(output_path=os.path.join("img2", "clustering_elbow_curve.jpg"))

# 比较聚类内均值与全局均值
# Compare intra-cluster means to global means
print(cl.compare_cluster_means_to_global_means())
cl.plot_cluster_means_to_global_means_comparison(xlabel='Principal Components', ylabel='Clusters',
                                                 levels=[-1, -0.67, -0.3, -0.15, 0.15, 0.3, 0.67, 1],
                                                 output_path=os.path.join("img2", "clustering_intra_comparison.jpg"))

# 比较原始变量在各聚类中的分布
# Compare distributions of original variables by cluster
cl.plot_distribution_comparison_by_cluster(df_ext=df_[['ESCS', 'TEACHSUP']],
                                           output_path=os.path.join("img2", "clustering_distribution_comparison.jpg"))

# 2-D plots # 二维图
cl.plot_clusters_2D('dim_01', 'dim_02', output_path=os.path.join("img2", "clustering_2d_plots.jpg"))

# 比较原始分类变量在各聚类中的分布
# Comparison of original categorical variable distribution by cluster
print(cl.describe_clusters_cat(df_['IMMIG'], cat_name='IMMIG', normalize=True))
cl.plot_cat_distribution_by_cluster(df_['IMMIG'], cat_label='IMMIG', cluster_label='Student clusters',
                                    output_path=os.path.join("img2", "clustering_cat_comparison.jpg"))

# 将聚类分配给包含原始变量的数据框
# Assign clusters to data frame with original variables
df_['cluster'] = cl.df['cluster'].values
df_['cluster_cat'] = cl.df['cluster_cat'].values

# CLASSIFIER # 分类器
print('--- CLASSIFIER 分类---')
from clearn.classifier import Classifier
np.random.seed(42)

# 用原始变量实例化类。将上面计算的聚类设置为目标
# Instantiate the class with the original variables. As target, we set the clusters computed above
var_list = list(df_.columns[1:-3])
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
classifier.train_model(features_to_keep=['ESCS'], hyperparameter_tuning=True,
                       param_grid=dict(n_estimators=[30, 60], eta=[0.15, 0.25], max_depth=[3, 5, 7]))

# 获取五个最重要特征的全局特征重要性
# Get global feature importance of the five most important features
print(classifier.feature_importances.head())

# 绘制全局特征重要性
# Plot global feature importance
classifier.plot_shap_importances(output_path=os.path.join("img2", "classifier_global_feature_importance.jpg"))
plt.clf()

# 绘制标识符为 1 和 2 的聚类的局部重要性
# Plot local importance for clusters with identifiers 1 and 2
classifier.plot_shap_importances_beeswarm(class_id=1,
                                          output_path=os.path.join("img2", "classifier_local_importance_cl1.jpg"))
plt.clf()
classifier.plot_shap_importances_beeswarm(class_id=2,
                                          output_path=os.path.join("img2", "classifier_local_importance_cl2.jpg"))
plt.clf()

# Performance assessment # 性能评估
# Hyperparameter tuning results # 超参数调整结果
print(classifier.hyperparameter_tuning_metrics())

# Confusion matrix # 混淆矩阵
classifier.plot_confusion_matrix(output_path=os.path.join("img2", "classifier_confusion_matrix.jpg"))

# Classification report # 分类报告
print(classifier.classification_report())

# ROC curves # ROC 曲线
classifier.plot_roc_curves(output_path=os.path.join("img2", "classifier_roc_curves.jpg"))







