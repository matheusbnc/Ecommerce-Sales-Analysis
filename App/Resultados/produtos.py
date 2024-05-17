#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from functions.functions import plot_bar
from time import sleep


# In[2]:

def more_units_sold(sales):
    sleep(0.5)
    
    sales = sales.groupby('Description').agg({'Quantity': 'sum'}).reset_index()
    
    sales = sales.sort_values(by=['Quantity'], ascending=False).reset_index(drop=True)
    
    plot_bar(sales, x_axes='Quantity', y_axes='Description', x_label='Quantidade Vendida'\
             ,y_label='Produto', title='Produtos Com Mais Unidades Vendidas'\
             ,palette='viridis')
    
    print(sales.head(15))

    
def more_profitable(sales):
    sleep(0.5)
    
    sales = sales.groupby('Description').agg({'FinalPrice': 'sum'}).reset_index()
    
    sales = sales.sort_values(by=['FinalPrice'], ascending=False).reset_index(drop=True)
    
    plot_bar(sales, x_axes='FinalPrice', y_axes='Description', x_label='Valor Total (£)'\
             ,y_label='Produto', title='Produtos Mais Rentáveis'\
             ,palette='viridis')
    
    print(sales.head(15))

    
def frequent_sales(sales):
    sleep(0.5)
    
    sales = sales[sales['Quantity'] > 0].groupby('Description')\
                        .agg({'InvoiceNo': 'count'}).reset_index()
    
    sales = sales.sort_values(by=['InvoiceNo'], ascending=False).reset_index(drop=True)
    
    plot_bar(sales, x_axes='InvoiceNo', y_axes='Description', x_label='Ocorrências'\
             ,y_label='Produto', title='Produtos com Mais Ocorrências de Compra'\
             ,palette='viridis')
    
    print(sales.head(15))

    
def more_units_canceled(sales): 
    sleep(0.5)
    
    sales = sales[sales['InvoiceNo'].str.startswith('C')].groupby('Description')\
                        .agg({'Quantity':'sum'}).abs().reset_index()
    
    sales = sales.sort_values(by=['Quantity'], ascending=False).reset_index(drop=True)
    
    plot_bar(sales, x_axes='Quantity', y_axes='Description', x_label='Quantidade Cancelada'\
             ,y_label='Produto', title='Produtos Com Mais Unidades Canceladas'\
             ,palette='rocket_r')
    
    print(sales.head(15))
 

def expensive_cancellations(sales):
    sleep(0.5)
    
    sales = sales[sales['InvoiceNo'].str.startswith('C')].groupby('Description')\
                        .agg({'FinalPrice': 'sum'}).abs().reset_index()
    
    sales = sales.sort_values(by=['FinalPrice'], ascending=False).reset_index(drop=True)
    
    plot_bar(sales, x_axes='FinalPrice', y_axes='Description', x_label='Valor Total (£)'\
             ,y_label='Produto', title='Produtos com Maiores Valores de Cancelamento'\
             ,palette='rocket_r')
    
    print(sales.head(15))    
    
    
def frequent_cancellations(sales):
    sleep(0.5)
    
    sales = sales[sales['InvoiceNo'].str.startswith('C')].groupby('Description')\
                        .agg({'InvoiceNo':'count'}).abs().reset_index()
    
    sales = sales.sort_values(by=['InvoiceNo'], ascending=False).reset_index(drop=True)
    
    plot_bar(sales, x_axes='InvoiceNo', y_axes='Description', x_label='Quantidade Cancelada'\
             ,y_label='Produto', title='Produtos Com Mais Ocorrências de Cancelamento'\
             ,palette='rocket_r', space=1)
    
    print(sales.head(15))    
    
# In[ ]:




