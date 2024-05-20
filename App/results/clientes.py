import pandas as pd
import numpy as np
from functions.functions import plot_bar, data_summary
from time import sleep


def more_units_sold_clients(sales_cli):
    sleep(0.5)
    
    sales_cli = sales_cli.groupby('CustomerID').agg({'Quantity': 'sum'}).reset_index()
    
    sales_cli = sales_cli.sort_values(by=['Quantity'], ascending=False).reset_index(drop=True)
    
    plot_bar(sales_cli, x_axes='Quantity', y_axes='CustomerID', x_label='Quantidade Vendida'\
             ,y_label='ID Cliente', title='Clientes com Mais Unidades Adquiridas'\
             ,palette='crest')
    
    data_summary(sales_cli)

def more_profitable_clients(sales_cli):
    sleep(0.5)
    
    sales_cli = sales_cli.groupby('CustomerID').agg({'FinalPrice': 'sum'}).reset_index()
    
    sales_cli = sales_cli.sort_values(by=['FinalPrice'], ascending=False).reset_index(drop=True)
    
    plot_bar(sales_cli, x_axes='FinalPrice', y_axes='CustomerID', x_label='Valor Total (£)'\
             ,y_label='ID Cliente', title='Clientes que Geraram Mais Receita'\
             ,palette='crest')
    
    data_summary(sales_cli)    
    

def frequent_clients(sales_cli):
    sleep(0.5)
    
    sales_cli = sales_cli[sales_cli['Quantity'] > 0].groupby('CustomerID')\
                                                .agg({'InvoiceNo': 'count'}).reset_index()
    
    sales_cli = sales_cli.sort_values(by=['InvoiceNo'], ascending=False).reset_index(drop=True)
    
    plot_bar(sales_cli, x_axes='InvoiceNo', y_axes='CustomerID', x_label='Ocorrências'\
             ,y_label='ID Cliente', title='Clientes com Mais Ocorrências de Compra'\
             ,palette='crest')
    
    data_summary(sales_cli)
    
    
def more_units_canceled_clients(sales_cli):
    sleep(0.5)
    
    sales_cli = sales_cli[sales_cli['InvoiceNo'].str.startswith('C')].groupby('CustomerID')\
                        .agg({'Quantity':'sum'}).abs().reset_index()
    
    sales_cli = sales_cli.sort_values(by=['Quantity'], ascending=False).reset_index(drop=True)
    
    plot_bar(sales_cli, x_axes='Quantity', y_axes='CustomerID', x_label='Quantidade Cancelada'\
             ,y_label='ID Cliente', title='Clientes Com Mais Unidades Canceladas'\
             ,palette='flare')
    
    data_summary(sales_cli)
    
    
def expensive_cancellations_clients(sales_cli):
    sleep(0.5)
    
    sales_cli = sales_cli[sales_cli['InvoiceNo'].str.startswith('C')].groupby('CustomerID')\
                        .agg({'FinalPrice':'sum'}).abs().reset_index()
    
    sales_cli = sales_cli.sort_values(by=['FinalPrice'], ascending=False).reset_index(drop=True)
    
    plot_bar(sales_cli, x_axes='FinalPrice', y_axes='CustomerID', x_label='Valor Total (£)'\
             ,y_label='ID Cliente', title='Clientes Com Maiores Valores de Cancelamento'\
             ,palette='flare')
    
    data_summary(sales_cli)
    
    
def frequent_cancellations_clients(sales_cli):
    sleep(0.5)
    
    sales_cli = sales_cli[sales_cli['InvoiceNo'].str.startswith('C')].groupby('CustomerID')\
                        .agg({'InvoiceNo':'count'}).abs().reset_index()
    
    sales_cli = sales_cli.sort_values(by=['InvoiceNo'], ascending=False).reset_index(drop=True)
    
    plot_bar(sales_cli, x_axes='InvoiceNo', y_axes='CustomerID', x_label='Ocorrências'\
             ,y_label='ID Cliente', title='Clientes Com Mais Ocorrências de Cancelamento'\
             ,palette='flare', space=1)
    
    data_summary(sales_cli)    