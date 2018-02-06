# 数据导入
import pandas as pd
wines = pd.read_csv("data/wines.csv")
print(wines.head())

# 变量之间的相关性分析
import matplotlib.pyplot as plt
import seaborn as sns
corr = wines.corr()
sns.heatmap(
    corr,
    xticklabels=corr.columns.values,
    yticklabels=corr.columns.values
)
plt.show()

