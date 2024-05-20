#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


def not_number(value):
    return not value[0].isdigit()


# In[3]:


def pre_processing(sales):
    
    # Filtra todos os registros que não vendas/cancelamento de produtos
    not_product_lines = sales[sales['StockCode'].apply(not_number)]

    # Obter os valores únicos das linhas
    not_product = not_product_lines['StockCode'].unique()
    
    sales = sales[~sales['StockCode'].isin(not_product)]
    
    # Adicionando coluna de Preço Final de venda/devolução para cada transação
    sales['FinalPrice'] = sales['Quantity'] * sales['UnitPrice']
    
    # Excluindo os registros com valor unitário igual a zero
    sales = sales[sales['UnitPrice'] > 0]
    
    # Remove as linhas duplicadas 
    sales = sales.drop_duplicates()
    
    # Converte a primeira letra de cada palavra para maíuscula em uma coluna específica de um dataframe
    title_col(sales)
    
    return sales


# In[4]:


def drop_nan(data, col_name='CustomerID'):
    data = data.drop(data[data['CustomerID'] == 'nan'].index)
    return data


# In[5]:


def title_col(data, col_name='Description'):
    '''
    Converte a primeira letra de cada palavra para maíuscula em uma coluna específica de um dataframe
    
    Parâmetros:
    -----------    
    data : pandas.DataFrame
        O DataFrame onde a coluna está localizada
    col_name : str
        A coluna que será transformada. Deve ser string.
    '''
    data[col_name] = data[col_name].apply(lambda x: x.title())
    return data


# In[6]:


def change_types(sales):
    sales['InvoiceDate'] = pd.to_datetime(sales['InvoiceDate'], format = '%d/%m/%Y %H:%M').dt.date
    sales['CustomerID'] = sales['CustomerID'].astype('str')
    sales['CustomerID'] = sales['CustomerID'].apply(lambda x: x.split('.')[0])
    sales['Country'] = sales['Country'].astype('str')


# In[ ]:




