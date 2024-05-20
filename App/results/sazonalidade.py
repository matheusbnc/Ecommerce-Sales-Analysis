#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
from functions.functions import plot_line, data_summary, group_data
from time import sleep


# In[ ]:


def daily_variation_quantity(sales_saz):
    sleep(0.5)
    
    sales_var = group_data(sales_saz, group_col='Day', operation_col='Quantity'\
                       ,operation='sum', how='sales')
    sales_var['Type'] = 'Unidades Vendidas'
    
    cancellations_var = group_data(sales_saz, group_col='Day', operation_col='Quantity'\
                       ,operation='sum', how='cancellations')
    cancellations_var['Type'] = 'Unidades Canceladas'
    
    combined_data = pd.concat([sales_var, cancellations_var], ignore_index=True)
    
    print(combined_data)
    
# In[ ]:




