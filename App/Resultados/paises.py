#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
from functions.functions import plot_bar
from time import sleep


# In[ ]:

def drop_uk(sales_ctr):
    sales_ctr = sales_ctr.drop(sales_ctr[sales_ctr['Country'] == 'United Kingdom'].index)
    return sales_ctr

def more_units_sold_country(sales_ctr):
    sleep(0.5)
    
    sales_ctr = sales_ctr.groupby('Country').agg({'Quantity': 'sum'}).reset_index()
    
    sales_ctr = sales_ctr.sort_values(by=['Quantity'], ascending=False).reset_index(drop=True)
    
    plot_bar(sales_ctr, x_axes='Quantity', y_axes='Country', x_label='Quantidade Vendida'\
             ,y_label='Country', title='Países com Mais Unidades Adquiridas'\
             ,palette='crest')
    
    print(sales_ctr.head(15))

def more_profitable_country(sales_ctr):
    sleep(0.5)
    
    sales_ctr = sales_ctr.groupby('Country').agg({'FinalPrice': 'sum'}).reset_index()
    
    sales_ctr = sales_ctr.sort_values(by=['FinalPrice'], ascending=False).reset_index(drop=True)
    
    plot_bar(sales_ctr, x_axes='FinalPrice', y_axes='Country', x_label='Valor Total (£)'\
             ,y_label='Country', title='Países que Geraram Maior Receita'\
             ,palette='crest')
    
    print(sales_ctr.head(15))
# In[ ]:




