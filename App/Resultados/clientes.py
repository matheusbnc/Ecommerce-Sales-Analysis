#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np
from functions.functions import plot_bar
from time import sleep


# In[5]:


def more_units_sold_clients(sales_cli):
    sleep(0.5)
    
    sales_cli = sales_cli.groupby('CustomerID').agg({'Quantity': 'sum'}).reset_index()
    
    sales_cli = sales_cli.sort_values(by=['Quantity'], ascending=False).reset_index(drop=True)
    
    plot_bar(sales_cli, x_axes='Quantity', y_axes='CustomerID', x_label='Quantidade Vendida'\
             ,y_label='CustomerID', title='Clientes com Mais Unidades Adquiridas'\
             ,palette='crest')
    
    print(sales_cli.head(15))

def more_profitable_clients(sales_cli):
    sleep(0.5)
    
    sales_cli = sales_cli.groupby('CustomerID').agg({'FinalPrice': 'sum'}).reset_index()
    
    sales_cli = sales_cli.sort_values(by=['FinalPrice'], ascending=False).reset_index(drop=True)
    
    plot_bar(sales_cli, x_axes='FinalPrice', y_axes='CustomerID', x_label='Valor Total (£)'\
             ,y_label='Cliente', title='Clientes que Geraram Mais Receita'\
             ,palette='crest')
    
    print(sales_cli.head(15))    
    

def frequent_clients(sales_cli):
    sleep(0.5)
    
    sales_cli = sales_cli[sales_cli['Quantity'] > 0].groupby('CustomerID')\
                                                .agg({'InvoiceNo': 'count'}).reset_index()
    
    sales_cli = sales_cli.sort_values(by=['InvoiceNo'], ascending=False).reset_index(drop=True)
    
    plot_bar(sales_cli, x_axes='InvoiceNo', y_axes='CustomerID', x_label='Ocorrências'\
             ,y_label='Cliente', title='Clientes com Mais Ocorrências de Compra'\
             ,palette='crest')
    
    print(sales_cli.head(15))  
# In[ ]:




