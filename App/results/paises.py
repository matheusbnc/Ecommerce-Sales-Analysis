import pandas as pd
import numpy as np
from functions.functions import plot_bar, data_summary
from time import sleep


def more_units_sold_country(sales_ctr):
    sleep(0.5)
    
    sales_ctr = sales_ctr.groupby('Country').agg({'Quantity': 'sum'}).reset_index()
    
    sales_ctr = sales_ctr.sort_values(by=['Quantity'], ascending=False).reset_index(drop=True)
    
    plot_bar(sales_ctr, x_axes='Quantity', y_axes='Country', x_label='Quantidade Vendida'\
             ,y_label='País', title='Países Estrangeiros com Mais Unidades Adquiridas'\
             ,palette='plasma')
    
    data_summary(sales_ctr)

def more_profitable_country(sales_ctr):
    sleep(0.5)
    
    sales_ctr = sales_ctr.groupby('Country').agg({'FinalPrice': 'sum'}).reset_index()
    
    sales_ctr = sales_ctr.sort_values(by=['FinalPrice'], ascending=False).reset_index(drop=True)
    
    plot_bar(sales_ctr, x_axes='FinalPrice', y_axes='Country', x_label='Valor Total (£)'\
             ,y_label='País', title='Países Estrangeiros que Geraram Maior Receita'\
             ,palette='plasma')
    
    data_summary(sales_ctr)
    

def frequent_sales_country(sales_ctr):
    sleep(0.5)
    
    sales_ctr = sales_ctr[sales_ctr['Quantity'] > 0].groupby('Country')\
                        .agg({'InvoiceNo': 'count'}).reset_index()
    
    sales_ctr = sales_ctr.sort_values(by=['InvoiceNo'], ascending=False).reset_index(drop=True)
    
    plot_bar(sales_ctr, x_axes='InvoiceNo', y_axes='Country', x_label='Ocorrências'\
             ,y_label='País', title='Países Estrangeiros com Mais Ocorrências de Compra'\
             ,palette='plasma')
    
    data_summary(sales_ctr)
def more_units_canceled_country(sales_ctr):
    sleep(0.5)
    
    sales_ctr = sales_ctr[sales_ctr['InvoiceNo'].str.startswith('C')].groupby('Country')\
                        .agg({'Quantity':'sum'}).abs().reset_index()
    
    sales_ctr = sales_ctr.sort_values(by=['Quantity'], ascending=False).reset_index(drop=True)
    
    plot_bar(sales_ctr, x_axes='Quantity', y_axes='Country', x_label='Quantidade Cancelada'\
             ,y_label='País', title='Países Estrangeiros com Mais Unidades Canceladas'\
             ,palette='cividis')
    
    data_summary(sales_ctr)
    
    
def expensive_cancellations_country(sales_ctr):
    sleep(0.5)
    
    sales_ctr = sales_ctr[sales_ctr['InvoiceNo'].str.startswith('C')].groupby('Country')\
                        .agg({'FinalPrice':'sum'}).abs().reset_index()
    
    sales_ctr = sales_ctr.sort_values(by=['FinalPrice'], ascending=False).reset_index(drop=True)
    
    plot_bar(sales_ctr, x_axes='FinalPrice', y_axes='Country', x_label='Valor Total (£)'\
             ,y_label='País', title='Países Estrangeiros Com Maiores Valores de Cancelamento'\
             ,palette='cividis')
    
    data_summary(sales_ctr)
    
    
def frequent_cancellations_country(sales_ctr):
    sleep(0.5)
    
    sales_ctr = sales_ctr[sales_ctr['InvoiceNo'].str.startswith('C')].groupby('Country')\
                        .agg({'InvoiceNo':'count'}).abs().reset_index()
    
    sales_ctr = sales_ctr.sort_values(by=['InvoiceNo'], ascending=False).reset_index(drop=True)
    
    plot_bar(sales_ctr, x_axes='InvoiceNo', y_axes='Country', x_label='Ocorrências'\
             ,y_label='País', title='Países Estrangeiros Com Mais Ocorrências de Cancelamento'\
             ,palette='cividis', space=1)
    
    data_summary(sales_ctr)    