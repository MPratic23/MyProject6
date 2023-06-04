#!/usr/bin/env python
# coding: utf-8

# In[1]:





# In[2]:


import pandas as pd
import streamlit as st


# In[3]:


df = pd.read_csv('vehicles_us.csv')
df = df.drop(df.columns[0], axis=1)


# In[4]:

# In[5]:
df["odometer"] = df.groupby("days_listed")['odometer'].transform(lambda x: x.fillna(x.mean()))

df["is_4wd"] = df.groupby("type")['is_4wd'].transform(lambda x: x.fillna(x.mean()))

df["model_year"] = df.groupby("date_posted")['model_year'].transform(lambda x: x.fillna(x.mean()))

df["cylinders"] = df.groupby("model")['cylinders'].transform(lambda x: x.fillna(x.mean()))

# In[6]:


st.header('Advertisement of used automobiles')

st.write("""
##### Filter the data below to view by year produced
""")

show_excellent_cars = st.checkbox('Include cars with excellent status')
if not show_excellent_cars:
    df = df[df.condition!='excellent']


# In[7]:




# In[8]:


model_choice = df['model'].unique()
make_choice_man = st.selectbox('Select model A:', model_choice)

model_choice = df['model'].unique()
man_option = st.selectbox('Select model B:', model_choice)

# In[9]:

# In[10]:


min_year, max_year=int(df['model_year'].min()), int(df['model_year'].max())

year_range = st.slider(
    "Choose year listed",
    value=(min_year, max_year),min_value=min_year, max_value=max_year)

actual_range=list(range(year_range[0],year_range[1]+1))


# In[11]:


year_range


# In[12]:


filtered_type=df[(df.model==make_choice_man) | (df.model==man_option) & (df.model_year.isin(list(actual_range)))]

st.table(filtered_type)


# In[13]:



# In[14]:


st.header('Inquiry of Purchase')

st.write("""
###### What determines the purchase of an automobile? We'll look at the distribution between component parts.
""")

import plotly.express as px

list_for_hist=['type', 'cylinders', 'is_4wd', 'transmission']
choice_for_hist = st.selectbox('Seperated by type ', list_for_hist)
fig1 = px.histogram(df, x='odometer', color=choice_for_hist)

fig1.update_layout(
title="<b> Seperated by component {}<b>".format(choice_for_hist))
st.plotly_chart(fig1)


# In[15]:


df['date']=2022-df['days_listed']
def day_category(x):
    if x<5: return '<5'
    elif x>=5 and x<10: return '5-10'
    elif x>=10 and x<20: return '10-20'
    else: return '>20'
df['day_category']= df['date'].apply(day_category)

st.write("""
##### How the model type is affected by days on market.
""")

list_for_scatter=['model', 'type', 'model_year']
choice_for_scatter = st.selectbox('Purchase depends on ', list_for_scatter)
fig2 = px.scatter(df, x='days_listed', color=choice_for_scatter, hover_data=['date_posted'])

fig2.update_layout(
title="Days on market versus {}".format(choice_for_scatter))
st.plotly_chart(fig2)

# In[ ]: