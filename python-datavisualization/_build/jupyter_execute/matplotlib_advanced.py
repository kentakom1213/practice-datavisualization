#!/usr/bin/env python
# coding: utf-8

# # Matplotlib（応用編）
# 
# [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)]()
# 
# 実際のデータから、プロットをしてみよう！
# 
# オブジェクト指向インターフェースを軽く使ってみます。

# In[1]:


import matplotlib.pyplot as plt
import pandas as pd


# ## データの読み込み

# In[2]:


# colabでは不要
get_ipython().system('mkdir -p sample_data')
get_ipython().system('curl -o "sample_data/california_housing_train.csv" -sL https://download.mlcc.google.com/mledu-datasets/california_housing_train.csv')


# In[3]:


df = pd.read_csv('sample_data/california_housing_train.csv')

df.head(5)


# ## 図の作成

# In[4]:


fig = plt.figure(figsize=(16, 8))

ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)


# **複数プロット**
# 
# ```python
# fig = plt.figure()
# ```
# 
# ↑新しい図（figureオブジェクト）を作成する。
# 
# ```python
# ax1 = fig.add_subplot(1, 2, 1)
# ax2 = fig.add_subplot(1, 2, 2)
# ```
# 
# ↑figを1行2列に分けて、`ax1`その1つ目（左側）に、`ax2`を2つ目（右側）に割り当てる。

# ## 散布図のプロット
# 
# 左側の図（`ax1`）に散布図をプロットしてみます。
# 
# **データ**
# - 横軸：所得の中央値
# - 縦軸：家賃の中央値

# In[5]:


ax1.scatter(df['median_income'], df['median_house_value'], c="tab:blue")

ax1.set_title("Income and HouseValue")  # 散布図のタイトル
ax1.set_xlabel("median income")         # x軸のラベル
ax1.set_ylabel("median house value")    # y軸のラベル

fig


# ### 箱ひげ図のプロット
# 
# 右側の図（`ax2`）に箱ひげ図をプロットしてみます。
# 
# **データ**
# - 家賃の中央値

# In[6]:


ax2.boxplot(df['median_house_value'])

ax2.set_title("House Value")

fig


# 割といい感じの図ができたんじゃないでしょうか？？
# 
# ## 参考
# 
# - [早く知っておきたかったmatplotlibの基礎知識、あるいは見た目の調整が捗るArtistの話 - Qiita](https://qiita.com/skotaro/items/08dc0b8c5704c94eafb9)
# - [matplotlib入門 - りんごがでている](https://bicycle1885.hatenablog.com/entry/2014/02/14/023734)