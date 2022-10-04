#!/usr/bin/env python
# coding: utf-8

# # Intermediate Jupyter Notebooks

# ## Bash!

# You can install libraries in the notebook, very useful for sharing code

# In[1]:


get_ipython().system(' pip install plotly dash')


# In[2]:


# List out a lot of the current files
get_ipython().system(' ls -l')


# In[3]:


get_ipython().run_cell_magic('bash', '', '\n# How much space is left on my computer?\ndf -h \n')


# ## Cross over between bash and python

# In[4]:


# Run the bash command `df -h` and store it in the python variable x
results = get_ipython().getoutput(' df -h')
results


# In[5]:


import re
import pandas as pd

# parse out the size, used, and avail
data = results[1:]
regexp = re.compile("(?P<filesystem>.*?)\s+(?P<size>.*?)\s+(?P<used>.*?)\s+(.*?)\s+(.*?)\s+(?P<mounted>.*)")

parsed_results = [regexp.match(l).groupdict() for l in data]
df = pd.DataFrame(parsed_results)
df


# In[6]:


mount_folder = df.loc[0, 'mounted']

print('What is in the mount folder:', mount_folder)
print('---')

get_ipython().system(' ls {mount_folder}')


# ## Jupyter magic
# There are lots of different ones, but here are some of my favourites

# In[7]:


get_ipython().run_cell_magic('time', '', 'import time\n\ntime.sleep(1)\nprint("hello world!")\n')


# In[8]:


import numpy as np

x = np.arange(1000)
get_ipython().run_line_magic('timeit', '-n 1000 np.sqrt(x)')


# ## Interative plots!
# 
# You can use libraries like plotly, which use HTML/JS to create interative plots

# In[9]:


import plotly.express as px
df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")
fig.show()


# ## Some debugging features
# 
# 
# You can click on debugging here, then open the tab
# ![](./assets/debugging-button.png)

# In[10]:


for k in [1, 5, 10, 0, 3]:
    print(1/k)


# ## Remote servers and google colab
# 
# Jupyter really runs a webserver, we don't have to be on the same device in order to access it (but by default you can't)
# 
# One example of using a remote jupyter notebook is google colab. Google provides free computing power that you can access from almost any device
# 
# You can also setup your own server and use port-forwarding to access it remotely (usually you also need to set server options such as `jupyter lab --ip 0.0.0.0` for things to work)
