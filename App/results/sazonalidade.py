#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
from functions.functions import plot_line, data_summary, group_data, order_days
from time import sleep


# In[ ]:


def daily_variation_quantity(sales_saz):
    sleep(0.5)
    
    sales_var = group_data(sales_saz, group_col='Day', operation_col='Quantity'\
                       ,operation='sum', how='sales')
    
    cancellations_var = group_data(sales_saz, group_col='Day', operation_col='Quantity'\
                       ,operation='sum', how='cancellations')
    
    sales_var = order_days(sales_var)
    cancellations_var = order_days(cancellations_var)
    
    plot_line(data1=sales_var, data2=cancellations_var, x_axes='Day', y_axes='Quantity'\
                      ,x_label='Dia', y_label='Unidades'\
                      ,title1='Total de Compras por Dia', title2='Total de Cancelamentos por Dia')

    
# In[ ]:




