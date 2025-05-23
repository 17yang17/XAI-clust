# Guides

This section contains five guides to help users get started with `clust-learn`. These guides are in `ipynb` and `html` format.
本节包含五个指南，帮助用户开始使用 `clust-learn` 。这些指南以 `ipynb` 和 `html` 格式提供。

_Note_ that the guides are designed so that the output of the data processing guide is subsequently used in the dimensionality reduction guide, and so on.
注意：指南被设计成数据处理指南的输出接着用于降维指南，依此类推。

## Table of guides

| Guide 指南 | Module 模块 | Description 描述 |
|:-|:-|:-|
| [`data_preprocessing_guide_default`](https://github.com/malgar/clust-learn/blob/master/notebooks/data_preprocessing_guide_default.ipynb) | [`data_preprocessing`](https://github.com/malgar/clust-learn/tree/master/clearn/data_preprocessing) | Perform data preprocessing in default mode. Recommended for beginners. 执行默认模式下的数据预处理。推荐初学者使用。 |
| [`data_preprocessing_guide_custom`](https://github.com/malgar/clust-learn/blob/master/notebooks/data_preprocessing_guide_custom.ipynb) | [`data_preprocessing`](https://github.com/malgar/clust-learn/tree/master/clearn/data_preprocessing) | Perform data preprocessing step by step with options to customize data imputation. Recommended for users who are familiar with the methodology. 逐步执行数据预处理步骤，并可选择自定义数据插补。适用于熟悉该方法的用户。 |
| [`dimensionality_reduction_guide`](https://github.com/malgar/clust-learn/blob/master/notebooks/dimensionality_reduction_guide.ipynb) | [`dimensionality_reduction`](https://github.com/malgar/clust-learn/tree/master/clearn/dimensionality_reduction) | Perform dimensionality reduction and explain how the new derived variables explain the original ones. 执行降维并解释新导出的变量如何解释原始变量。 |
| [`clustering_guide`](https://github.com/malgar/clust-learn/blob/master/notebooks/clustering_guide.ipynb)  | [`clustering`](https://github.com/malgar/clust-learn/tree/master/clearn/clustering) | Perfom cluster analysis, assess performance, and explain the obtained clusters with internal and external variables. 执行聚类分析，评估性能，并使用内部和外部变量解释获得的聚类。 |
| [`classifier_guide`](https://github.com/malgar/clust-learn/blob/master/notebooks/classifier_guide.ipynb) | [`classifier`](https://github.com/malgar/clust-learn/tree/master/clearn/classifier) | Perform classification, assess model performance, and explain results using SHAP values. This guide shows how to use the module to further explain the clusters obtained in the `clustering_guide`; however, the module may be used to fit any classificaton model 执行分类，评估模型性能，并使用 SHAP 值解释结果。本指南展示了如何使用该模块进一步解释在 `clustering_guide` 中获得的聚类；然而，该模块也可以用于拟合任何分类模型。 |


## Data

The data used in the five guides is available [here](https://github.com/malgar/clust-learn/tree/master/notebooks/data). You can find the output generated by each guide; these are used:

五篇指南中使用的数据在此处可用。您可以找到每个指南生成的输出；
这些被使用：
- as input of the subsequent modules, 作为后续模块的输入
- for reproducibility purposes. 为了可重复性目的。


## Reproducibility 可复现性

We have made the output of each module available for reproducibility purposes. Note that the `numpy` seed is set in each guide to ensure that the same results are generated.
我们已经将每个模块的输出提供出来，以便于重现。请注意，在每个指南中已设置 numpy 种子，以确保生成相同的结果。

The guides were originally run on a 64-bit Microsoft Operating System.
指南最初是在 64 位微软操作系统上运行的。
