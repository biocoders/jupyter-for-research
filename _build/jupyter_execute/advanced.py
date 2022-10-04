#!/usr/bin/env python
# coding: utf-8

# # Advanced Jupyter Topics

# ## Open in Colab button
# 
# [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/biocoders/jupyter-for-research/blob/master/advanced.ipynb)

# ## Widgets and Dashboards

# In[1]:


from ipywidgets import Button, IntText, Label, VBox, HBox

button = Button()
button.description = "Click me!"

output = IntText()
output.value = 0

def update_counter(evt):
    output.value += 1

button.on_click(update_counter)
HBox([Label("Number of clicks"), output, button])


# ## Voila example
# 
# ![](./assets/demo-dashboard.gif)

# ## Jupyter Books
# 
# Jupyter books are a popular way to create documentation for projects with working code examples
# 
# An example of this is the current deeplabcut docs:
# https://deeplabcut.github.io/DeepLabCut/README.html
# 
# ![](./assets/dlc-jupyterbooks.png)

# This project also uses jupyter books!
# 
# You can see it published here
# 
# For instructions on how to use it with github (/gitpages), look here: https://jupyterbook.org/en/stable/publish/gh-pages.html
