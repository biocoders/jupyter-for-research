#!/usr/bin/env python
# coding: utf-8

# # Introduction to Jupyter

# ## Writing code
# 
# Code in jupyter can be written as a bunch of cells

# In[1]:


x = 5
print(x)


# In[2]:


x = 10
x # jupyter will just print out any variables you put at the end of the block


# In[3]:


# You can also run blocks repeatedly and out of order
x = x + 3
print(x)


# ## Markdown
# One of the features of Jupyter notebooks is that you can write blocks of text like this!

# ### Code blocks (except as text)
# Markdown has a ton of features, one of the first ones I'll use is the code feature. You can write a code block like this by surrounding it in "```"
# 
# For example, to recreate the first cell, we can do 
# ```markdown
# ## Markdown
# One of the features of Jupyter notebooks is that you can write blocks of text like this!
# 
# Markdown has a ton of features, one of the first ones I'll use is the code feature. You can write a code block like this by surrounding it in "```"
# ```

# ### Images!
# You can include images like this!
# ```
# ![](./assets/hiking-evans-peak.jpg)
# ```
# 
# ![](./assets/hiking-evans-peak.jpg)
# 
# (Also video and audio!)

# ## HTML
# There are a few ways to throw html into Jupyter
# 
# For a lot of html, you can just write it like normal, for example 
# 
# <a href="http://example.com">This is a link!</a> 
# could be written as `<a href="http://example.com">This is a link!</a>`   
# (or in markdown `[This is a link!](http://example.com)`)
# 
# 
# For more complicated things, you can create HTML cells like below

# In[4]:


get_ipython().run_cell_magic('html', '', '<iframe width="560" height="315" src="https://www.youtube.com/embed/52Gg9CqhbP8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>\n')


# ## $\LaTeX$ Equations
# You can also write $\LaTeX$ (latex) in markdown cells! Latex is often used to render formulas. This is a great way to show an equation or algorithm you've written code for.
# 
# Here's one you may be familiar with
# $$ 
# \begin{bmatrix}
# w_0 & w_1 & w_2
# \end{bmatrix}
# \begin{bmatrix}
# x_0 \\ x_1 \\ x_2
# \end{bmatrix}
# + 
# \begin{bmatrix}
# b_0 \\ b_1 \\ b_2
# \end{bmatrix}
# =
# \begin{bmatrix}
# y_0 \\ y_1 \\ y_2
# \end{bmatrix}
# $$
# 
# But have seen this one before? 
# $$
# i \hbar \frac{\partial}{\partial t}\Psi(\mathbf{r},t) = \hat H \Psi(\mathbf{r},t)
# $$

# ### Tables
# I find markdown tables a little inconvenient to create myself, but you can use tools to generate them and just paste them in
# 
# | | x| y|
# |---|---|---|
# |0|0.2|1.2|
# |1|0.6|2.8|
# |2|0.3|0.4|
# |3|0.1|0.2|

# ## What are some things that make Jupyter great for researchers?
# 
# One big thing is that a lot of new work requires exploration. Jupyter notebooks are great at rapid exploration as you can split up your cells and focus on specific topics.

# ### Displaying plots

# In[5]:


import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 0.25, 1000)

plt.title("Coding ability as a function of blood alcohol %")
plt.plot(x, np.exp(-x*10), label="Actual")
plt.plot(x, 1+(x*5)**2, label="Perceived")
plt.ylabel("Coding Productivity")
plt.xlabel("Blood alcohol %")
plt.legend()


# Credit: https://xkcd.com/323/ (this is just my take on a popular xkcd comic)

# ### Displaying tables

# In[6]:


import pandas as pd

df = pd.read_csv("./assets/iris.csv")
df


# In[7]:


import seaborn as sns

sns.scatterplot(data=df, x='petal.length', y='sepal.length', hue='variety')


# You can make things look nice!

# In[8]:


import time
from tqdm.notebook import tqdm

for i in tqdm(range(1000)):
    time.sleep(0.001)

