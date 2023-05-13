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


df


# In[5]:


df.shape


# In[6]:


st.header('Advertisement of used automobiles')

st.write("""
##### Filter the data below to view by year produced
""")

show_excellent_cars = st.checkbox('Include cars with excellent status')
if not show_excellent_cars:
    df = df[df.condition!='excellent']


# In[7]:


show_excellent_cars


# In[8]:


model_choice = df['model'].unique()
make_choice_man = st.selectbox('Select model:', model_choice)


# In[9]:


make_choice_man


# In[10]:


min_year, max_year=int(df['model_year'].min()), int(df['model_year'].max())

year_range = st.slider(
    "Choose year listed",
    value=(min_year, max_year),min_value=min_year, max_value=max_year)

actual_range=list(range(year_range[0],year_range[1]+1))


# In[11]:


year_range


# In[12]:


filtered_type=df[(df.model==make_choice_man) & (df.model_year.isin(list(actual_range)))]

st.table(filtered_type)


# In[13]:


filtered_type


# In[14]:


st.header('Inquiry of Purchase')

st.write("""
###### What effects the purchase of an automobile? We'll look at the distribution between transmission type, amount of cylinders, and odometer reading.
""")

import plotly.express as px

list_for_hist=['transmission', 'cylinders', 'odometer']
choice_for_hist = st.selectbox('Seperated by transmission, cylinders, odometer', list_for_hist)
fig1 = px.histogram(df, x='odometer', color=choice_for_hist)

fig1.update_layout(
title="<b> Seperated by component {}<b>".format(choice_for_hist))
st.plotly_chart(fig1)


# In[15]:


df['time']=2023-df['days_listed']

def days_listed(x):
    if x<5: return '<5'
    elif x>=5 and x<10: return '5-10'
    elif x>=10 and x<20: return '10-20'
    else: return '>20'
        
df['model_year']= df['time'].apply(days_listed)


# In[16]:


st.write("""
##### How the model type is affected by its age.
""")

list_for_scatter=['model_year', 'days_listed', 'type']
choice_for_scatter = st.selectbox('Purchase depends on', list_for_scatter)
fig2 = px.scatter(df, x='model_year', y=choice_for_scatter, color="days_listed", hover_data=['type'])

fig2.update_layout(
title="<b> Model type versus model year (</b>" .format(choice_for_scatter))
st.plotly_chart(fig2)


# In[ ]:




