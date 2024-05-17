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


# In[ ]:




