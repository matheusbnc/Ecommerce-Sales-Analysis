#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from functions.functions import plot_bar, data_summary, group_data
from time import sleep


# In[2]:

def more_units_sold(sales_uni):
    sleep(0.5)
    
    sales_uni = group_data(sales_uni, group_col='Description', operation_col='Quantity'\
                       ,operation='sum', how='balance')
    
    plot_bar(sales_uni, x_axes='Quantity', y_axes='Description', x_label='Quantidade Vendida'\
             ,y_label='Produto', title='Produtos Com Mais Unidades Vendidas'\
             ,palette='viridis')
    
    data_summary(sales_uni)
    
def more_profitable(sales_uni):
    sleep(0.5)
    
    sales_uni = group_data(sales_uni, group_col='Description', operation_col='FinalPrice'\
                       ,operation='sum', how='balance')
    
    plot_bar(sales_uni, x_axes='FinalPrice', y_axes='Description', x_label='Valor Total (£)'\
             ,y_label='Produto', title='Produtos Mais Rentáveis'\
             ,palette='viridis')
    
    data_summary(sales_uni)

    
def frequent_sales(sales_uni):
    sleep(0.5)

    sales_uni = group_data(sales_uni, group_col='Description', operation_col='InvoiceNo'\
                       ,operation='count', how='sales')
    
    plot_bar(sales_uni, x_axes='InvoiceNo', y_axes='Description', x_label='Ocorrências'\
             ,y_label='Produto', title='Produtos com Mais Ocorrências de Compra'\
             ,palette='viridis')
    
    data_summary(sales_uni)

    
def more_units_canceled(sales_uni): 
    sleep(0.5)

    sales_uni = group_data(sales_uni, group_col='Description', operation_col='Quantity'\
                       ,operation='sum', how='cancellations')    
        
    plot_bar(sales_uni, x_axes='Quantity', y_axes='Description', x_label='Quantidade Cancelada'\
             ,y_label='Produto', title='Produtos Com Mais Unidades Canceladas'\
             ,palette='rocket_r')
    
    data_summary(sales_uni)
 

def expensive_cancellations(sales_uni):
    sleep(0.5)

    sales_uni = group_data(sales_uni, group_col='Description', operation_col='FinalPrice'\
                       ,operation='sum', how='cancellations')     
    
    plot_bar(sales_uni, x_axes='FinalPrice', y_axes='Description', x_label='Valor Total (£)'\
             ,y_label='Produto', title='Produtos com Maiores Valores de Cancelamento'\
             ,palette='rocket_r')
    
    data_summary(sales_uni)    
    
    
def frequent_cancellations(sales_uni):
    sleep(0.5)
    
    sales_uni = group_data(sales_uni, group_col='Description', operation_col='InvoiceNo'\
                       ,operation='count', how='cancellations') 
    
    plot_bar(sales_uni, x_axes='InvoiceNo', y_axes='Description', x_label='Quantidade Cancelada'\
             ,y_label='Produto', title='Produtos Com Mais Ocorrências de Cancelamento'\
             ,palette='rocket_r', space=1)
    
    data_summary(sales_uni)    
    
# In[ ]:




