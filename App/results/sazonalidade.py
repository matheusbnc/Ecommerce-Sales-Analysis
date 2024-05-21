#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
from functions.functions import plot_line, data_summary, group_data, order_days, order_months
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
                      ,title1='Variação Diária de Vendas', title2='Variação Diária de Cancelamentos')
    
def daily_variation_price(sales_saz):
    sleep(0.5)
    
    sales_var = group_data(sales_saz, group_col='Day', operation_col='FinalPrice'\
                       ,operation='sum', how='sales')
    
    cancellations_var = group_data(sales_saz, group_col='Day', operation_col='FinalPrice'\
                       ,operation='sum', how='cancellations')
    
    sales_var = order_days(sales_var)
    cancellations_var = order_days(cancellations_var)
    
    plot_line(data1=sales_var, data2=cancellations_var, x_axes='Day', y_axes='FinalPrice'\
                      ,x_label='Dia', y_label='Valor (£)'\
                      ,title1='Variação Diária de Vendas', title2='Variação Diária de Cancelamentos')

def daily_variation_frequency(sales_saz):
    sleep(0.5)
    
    sales_var = group_data(sales_saz, group_col='Day', operation_col='InvoiceNo'\
                       ,operation='count', how='sales')
    
    cancellations_var = group_data(sales_saz, group_col='Day', operation_col='InvoiceNo'\
                       ,operation='count', how='cancellations')
    
    sales_var = order_days(sales_var)
    cancellations_var = order_days(cancellations_var)
    
    plot_line(data1=sales_var, data2=cancellations_var, x_axes='Day', y_axes='InvoiceNo'\
                      ,x_label='Dia', y_label='Ocorrências'\
                      ,title1='Variação Diária de Vendas', title2='Variação Diária de Cancelamentos')    
    
def monthly_variation_quantity(sales_saz):
    sleep(0.5)
    
    sales_var = group_data(sales_saz, group_col='Month', operation_col='Quantity'\
                       ,operation='sum', how='sales')
    
    cancellations_var = group_data(sales_saz, group_col='Month', operation_col='Quantity'\
                       ,operation='sum', how='cancellations')
    
    sales_var = order_months(sales_var)
    cancellations_var = order_months(cancellations_var)    
    
    plot_line(data1=sales_var, data2=cancellations_var, x_axes='Month', y_axes='Quantity'\
                      ,x_label='Mês', y_label='Unidades'\
                      ,title1='Variação Mensal de Vendas', title2='Variação Mensal de Cancelamentos')
    
def monthly_variation_price(sales_saz):
    sleep(0.5)
    
    sales_var = group_data(sales_saz, group_col='Day', operation_col='FinalPrice'\
                       ,operation='sum', how='sales')
    
    cancellations_var = group_data(sales_saz, group_col='Day', operation_col='FinalPrice'\
                       ,operation='sum', how='cancellations')
    
    sales_var = order_days(sales_var)
    cancellations_var = order_days(cancellations_var)
    
    plot_line(data1=sales_var, data2=cancellations_var, x_axes='Day', y_axes='FinalPrice'\
                      ,x_label='Dia', y_label='Valor (£)'\
                      ,title1='Variação Diária de Vendas', title2='Variação Diária de Cancelamentos')

def monthly_variation_frequency(sales_saz):
    sleep(0.5)
    
    sales_var = group_data(sales_saz, group_col='Day', operation_col='InvoiceNo'\
                       ,operation='count', how='sales')
    
    cancellations_var = group_data(sales_saz, group_col='Day', operation_col='InvoiceNo'\
                       ,operation='count', how='cancellations')
    
    sales_var = order_days(sales_var)
    cancellations_var = order_days(cancellations_var)
    
    plot_line(data1=sales_var, data2=cancellations_var, x_axes='Day', y_axes='InvoiceNo'\
                      ,x_label='Dia', y_label='Ocorrências'\
                      ,title1='Variação Diária de Vendas', title2='Variação Diária de Cancelamentos')
    




