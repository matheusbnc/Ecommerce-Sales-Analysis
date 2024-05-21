import pandas as pd
import numpy as np
from functions.functions import plot_bar, data_summary, group_data
from time import sleep


def more_units_sold_clients(sales_cli):
    '''
    Plota e exibe um resumo dos clientes com maior saldo de unidades compradas,
    somando as vendas com os cancelamentos.
    
    Parâmetros:
        sales_cli (DataFrame): DataFrame contendo os dados de vendas por cliente.
    '''
    sleep(0.5)
    
    sales_cli = group_data(sales_cli, group_col='CustomerID', operation_col='Quantity'\
                       ,operation='sum', how='balance')    
    
    plot_bar(sales_cli, x_axes='Quantity', y_axes='CustomerID', x_label='Quantidade Vendida'\
             ,y_label='ID Cliente', title='Clientes com Mais Unidades Adquiridas'\
             ,palette='crest')
    
    data_summary(sales_cli)

def more_profitable_clients(sales_cli):
    '''
    Plota e exibe um resumo dos clientes que geraram maior receita final,
    somando as vendas com os cancelamentos.
    
    Parâmetros:
        sales_cli (DataFrame): DataFrame contendo os dados de vendas por cliente.
    '''
    sleep(0.5)
    
    sales_cli = group_data(sales_cli, group_col='CustomerID', operation_col='FinalPrice'\
                       ,operation='sum', how='balance') 
    
    plot_bar(sales_cli, x_axes='FinalPrice', y_axes='CustomerID', x_label='Valor Total (£)'\
             ,y_label='ID Cliente', title='Clientes que Geraram Mais Receita'\
             ,palette='crest')
    
    data_summary(sales_cli)    
    

def frequent_clients(sales_cli):
    '''
    Plota e exibe um resumo dos clientes com mais registros de compra,
    sem considerar cancelamentos.
    
    Parâmetros:
        sales_cli (DataFrame): DataFrame contendo os dados de vendas por cliente.
    '''
    sleep(0.5)
    
    sales_cli = group_data(sales_cli, group_col='CustomerID', operation_col='InvoiceNo'\
                       ,operation='count', how='sales')   
    
    plot_bar(sales_cli, x_axes='InvoiceNo', y_axes='CustomerID', x_label='Ocorrências'\
             ,y_label='ID Cliente', title='Clientes com Mais Ocorrências de Compra'\
             ,palette='crest')
    
    data_summary(sales_cli)
    
    
def more_units_canceled_clients(sales_cli):
    '''
    Plota e exibe um resumo dos clientes com mais unidades canceladas.
    
    Parâmetros:
        sales_cli (DataFrame): DataFrame contendo os dados de cancelamentos por cliente.
    '''
    sleep(0.5)
    
    sales_cli = group_data(sales_cli, group_col='CustomerID', operation_col='Quantity'\
                       ,operation='sum', how='cancellations')
    
    plot_bar(sales_cli, x_axes='Quantity', y_axes='CustomerID', x_label='Quantidade Cancelada'\
             ,y_label='ID Cliente', title='Clientes Com Mais Unidades Canceladas'\
             ,palette='flare')
    
    data_summary(sales_cli)
    
    
def expensive_cancellations_clients(sales_cli):
    '''
    Plota e exibe um resumo dos clientes com maiores valores de cancelamento.
    
    Parâmetros:
        sales_cli (DataFrame): DataFrame contendo os dados de cancelamentos por cliente.
    '''
    sleep(0.5)
    
    sales_cli = group_data(sales_cli, group_col='CustomerID', operation_col='FinalPrice'\
                       ,operation='sum', how='cancellations')
    
    plot_bar(sales_cli, x_axes='FinalPrice', y_axes='CustomerID', x_label='Valor Total (£)'\
             ,y_label='ID Cliente', title='Clientes Com Maiores Valores de Cancelamento'\
             ,palette='flare')
    
    data_summary(sales_cli)
    
    
def frequent_cancellations_clients(sales_cli):
    '''
    Plota e exibe um resumo dos clientes com mais registros de cancelamento.
    
    Parâmetros:
        sales_cli (DataFrame): DataFrame contendo os dados de cancelamentos por cliente.
    '''
    sleep(0.5)
    
    sales_cli = group_data(sales_cli, group_col='CustomerID', operation_col='InvoiceNo'\
                       ,operation='count', how='cancellations')        
    
    plot_bar(sales_cli, x_axes='InvoiceNo', y_axes='CustomerID', x_label='Ocorrências'\
             ,y_label='ID Cliente', title='Clientes Com Mais Ocorrências de Cancelamento'\
             ,palette='flare', space=1)
    
    data_summary(sales_cli)    