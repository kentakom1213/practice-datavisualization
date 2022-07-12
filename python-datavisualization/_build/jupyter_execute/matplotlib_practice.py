#!/usr/bin/env python
# coding: utf-8

# # 演習問題
# 
# [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/kentakom1213/practice-datavisualization/blob/main/matplotlib_practice.ipynb)
# 
# 演習問題です。
# 

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# In[2]:


df = pd.read_csv('sample_data/california_housing_train.csv')

print(df.head(5))


# In[3]:


fig = plt.figure(figsize=(12, 10))

ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
ax4 = fig.add_subplot(2, 2, 4)

# ax1 (左上)

# ax2 (右上)

# ax3 (左下)

# ax4 (右下)

