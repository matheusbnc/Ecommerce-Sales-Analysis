import pandas as pd
import numpy as np


def not_number(value):
    return not value[0].isdigit()


def title_col(data, col_name='Description'):
    '''
    Converte a primeira letra de cada palavra para maíuscula em uma coluna específica de um dataframe
    
    Parâmetros:
    -----------    
    data : pandas.DataFrame
        O DataFrame onde a coluna está localizada
    col_name : str
        A coluna que será transformada. Deve ser string.
    '''
    data[col_name] = data[col_name].apply(lambda x: x.title())
    return data


def pre_processing(data):
    
    # Filtra todos os registros que não vendas/cancelamento de produtos
    not_product_lines = data[data['StockCode'].apply(not_number)]

    # Obter os valores únicos das linhas
    not_product = not_product_lines['StockCode'].unique()
    
    data = data[~data['StockCode'].isin(not_product)]
    
    # Adicionando coluna de Preço Final de venda/devolução para cada transação
    data['FinalPrice'] = data['Quantity'] * data['UnitPrice']
    
    # Excluindo os registros com valor unitário igual a zero
    data = data[data['UnitPrice'] > 0]
    
    # Remove as linhas duplicadas 
    data = data.drop_duplicates()
    
    # Converte a primeira letra de cada palavra para maíuscula em uma coluna específica de um dataframe
    title_col(data)
    
    return data


def change_types(data):
    data['InvoiceDate'] = pd.to_datetime(data['InvoiceDate'], format = '%d/%m/%Y %H:%M')
    data['CustomerID'] = data['CustomerID'].astype('str')
    data['CustomerID'] = data['CustomerID'].apply(lambda x: x.split('.')[0])
    data['Country'] = data['Country'].astype('str')
    return data


def drop_uk(data):
    data = data.drop(data[data['Country'] == 'United Kingdom'].index)
    return data


def drop_nan(data, col_name='CustomerID'):
    data = data.drop(data[data['CustomerID'] == 'nan'].index)
    return data


def add_time_columns(data):
    data['Month'] = data['InvoiceDate'].dt.month_name(locale='pt_BR')
    data['Day'] = data['InvoiceDate'].dt.day_name(locale='pt_BR')
    data['Quarter'] = data['InvoiceDate'].dt.quarter.apply(lambda x: f'T{x}')
    data['Year'] = data['InvoiceDate'].dt.year
    return data

    




