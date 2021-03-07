#!/usr/bin/env python
# coding: utf-8

# My goal is to scrap the results table in this website and store it in a csv for easier manipulation using Python: https://www.footballhistory.org/tournament/champions-league.html

# Step 1: Import the necessary libraries and get the html of the page.
# Use urllib.request module to open URLs.
# The Beautiful Soup package is used to extract data from html files. The Beautiful Soup library’s name is bs4 which stands for Beautiful Soup, version 4.

# In[1]:


from urllib.request import urlopen
from bs4 import BeautifulSoup


# In[14]:


html = urlopen("https://www.footballhistory.org/tournament/champions-league.html")


# Step 2: Create a Beautiful Soup object from the html. Beautiful Soup package is used to take the raw html text and break it into Python objects (Parsing the data). It helps formatting and organizing the messy web by fixing bad HTML and presenting us with easily traversable Python objects.
# 

# In[15]:


bsobj = BeautifulSoup(html, 'lxml')
print(bsobj)


# There are two things to note in the above code. 1) we are converting the html data to a beautiful soup object. 2) lxml is a very useful XML/HTML processing library.

# Step3 : Store the target information. Our target is to take each row of data and store it in a csv file.

# In[16]:


table_rows= bsobj.findAll('tr')
print(table_rows)


# In[17]:


for row in table_rows:
    each_row= row.findAll('td')
    print(each_row)


# You want text without html tags. You can remove the html tags using BeautifulSoup.
# Note: You are doing two things here. 1) removing html tags using BeautifulSoup and extracting only text 2) Creating an empty list and appending each row of text to the empty list.

# In[18]:


lists_of_rows = []
for row in table_rows:
    each_row= row.findAll('td')
    str_row= str(each_row)
    row_text = BeautifulSoup(str_row, "lxml").get_text()
    lists_of_rows.append(row_text)
print(lists_of_rows)


# 4. The next step is to convert the list into a data frame and get the view of the rows using Pandas.

# In[19]:


import pandas as pd
import numpy as np


# In[67]:


data = pd.DataFrame(lists_of_rows[:29])
print(data)


# In[68]:


data.to_csv(r'C:\Users\Ashank S More\Desktop\webscraptrial3.csv', encoding='utf-8', index=False)


# In[69]:


df=pd.read_csv("webscraptrial3.csv")


# In[70]:


df.head()


# In[71]:


df2 = df['0'].str.split(', ', expand=True)


# In[72]:


df2


# In[73]:


df2.columns = ['Season', 'Winners','Runner-Up']


# In[74]:


df2.head()


# In[75]:


df2.sort_values('Season')


# In[92]:


data2 = pd.DataFrame(lists_of_rows[30:43])
print(data2)


# In[93]:


data2.to_csv(r'C:\Users\Ashank S More\Desktop\webscraptrial4.csv', encoding='utf-8', index=False)


# In[94]:


dfn=pd.read_csv("webscraptrial4.csv")


# In[95]:


dfn = dfn['0'].str.split(', ', expand=True)


# In[96]:


dfn.columns = ['Club', 'Titles','First']


# In[97]:


dfn.sort_values('Titles', ascending=False)

