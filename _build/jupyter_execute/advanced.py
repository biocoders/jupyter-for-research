#!/usr/bin/env python
# coding: utf-8

# # Advanced Jupyter Topics

# ## Widgets and Dashboards

# In[1]:


from ipywidgets import Button, IntText, Label, VBox, HBox

button = Button()
button.description = "Click me!"

output = IntText()
output.value = 0

def update_counter(evt):
    output.value += 1
    print(output.value)

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
