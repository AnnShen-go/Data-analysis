#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[5]:


raw_csv_data = pd.read_csv('Absenteeism_data.csv')
raw_csv_data


# In[7]:


df = raw_csv_data.copy()


# In[8]:


df


# In[68]:


pd.options.display.max_columns = None


# In[69]:


pd.options.display.max_rows = None


# In[70]:


display(df)


# In[14]:


df.info()


# In[23]:


df= df.drop(['ID'], axis=1)


# In[24]:


df


# In[27]:


df['Reason for Absence'].min()


# In[28]:


df['Reason for Absence'].max()


# In[29]:


df['Reason for Absence'].unique()


# In[30]:


len(df['Reason for Absence'].unique())


# In[31]:


sorted(df['Reason for Absence'].unique())


# In[57]:


reason_columns= pd.get_dummies(df['Reason for Absence'])
reason_columns


# In[61]:


reason_columns= pd.get_dummies(df['Reason for Absence'],drop_first = True)
reason_columns


# In[62]:


df.columns.values


# In[63]:


reason_columns.columns.values


# In[65]:


df=df.drop(['Reason for Absence'], axis=1)


# In[66]:


reason_type_1 = reason_columns.loc[:,1:14].max(axis=1)
reason_type_2 = reason_columns.loc[:,15:17].max(axis=1)
reason_type_3 = reason_columns.loc[:,18:21].max(axis=1)
reason_type_4 = reason_columns.loc[:,22:].max(axis=1)


# In[67]:


reason_type_1


# In[73]:


df= pd.concat([df, reason_type_1, reason_type_2, reason_type_3, reason_type_4],axis=1)
df


# In[ ]:


column_names= ['Date', 'Transportation Expense',
       'Distance to Work', 'Age', 'Daily Work Load Average',
       'Body Mass Index', 'Education', 'Children', 'Pets',
       'Absenteeism Time in Hours','Reason_1','Reason_2','Reason_3','Reason_4']


# In[74]:


df.columns=column_names


# In[77]:


df.head()


# In[80]:


column_names_reordered=['Reason_1','Reason_2','Reason_3','Reason_4','Date', 'Transportation Expense',
       'Distance to Work', 'Age', 'Daily Work Load Average',
       'Body Mass Index', 'Education', 'Children', 'Pets',
       'Absenteeism Time in Hours']


# In[81]:


df=df[column_names_reordered]


# In[82]:


df.head()


# In[133]:


df_reason_mod=df.copy()


# In[134]:


df_reason_mod


# In[87]:


df_reason_mod['Date']


# In[88]:


type(df_reason_mod['Date'][0])


# In[95]:


df_reason_mod['Date']= pd.to_datetime(df_reason_mod['Date'], format='%d/%m/%Y')


# In[96]:


df_reason_mod['Date']


# In[97]:


df_reason_mod['Date'][0]


# In[98]:


df_reason_mod['Date'][0].month


# In[99]:


list_months=[]
list_months


# In[100]:


df_reason_mod.shape


# In[102]:


for i in range(df_reason_mod.shape[0]):
    list_months.append(df_reason_mod['Date'][i].month)


# In[103]:


list_months


# In[104]:


len(list_months)


# In[105]:


df_reason_mod['Month Value']=list_months


# In[106]:


df_reason_mod.head(20)


# In[107]:


df_reason_mod['Date'][699].weekday()


# In[108]:


df_reason_mod['Date'][699]


# In[109]:


def date_to_weekday(date_value):
    return date_value.weekday()


# In[110]:


df_reason_mod['Day of the week']= df_reason_mod['Date'].apply(date_to_weekday)


# In[136]:


df_reason_mod.head()


# In[142]:


df_reason_date_mod = df_reason_mod.copy()


# In[143]:


df_reason_date_mod 


# In[145]:


df_reason_date_mod['Education'].unique() 


# In[146]:


df_reason_date_mod['Education'].value_counts()


# In[147]:


df_reason_date_mod['Education']=df_reason_date_mod['Education'].map({1:0,2:1,3:1,4:1})


# In[148]:


df_reason_date_mod['Education'].unique() 


# In[149]:


df_reason_date_mod['Education'].value_counts()


# In[150]:


df_preprocessed= df_reason_date_mod.copy()
df_preprocessed.head(10)


# In[ ]:




