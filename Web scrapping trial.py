#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd

from urllib.request import urlopen
from bs4 import BeautifulSoup


# In[2]:


def getHTMLContent(link):
    html = urlopen(link)
    soup = BeautifulSoup(html, 'html.parser')
    return soup


# In[3]:


content = getHTMLContent('https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population')
tables = content.find_all('table')
for table in tables:
    print(table.prettify())

