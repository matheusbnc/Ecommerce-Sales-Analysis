import pandas as pd
import numpy as np


def not_number(value):
    # Verifica se o valor não começa com um dígito
    return not value[0].isdigit()


def title_col(data, col_name='Description'):
    # Converte a primeira letra de cada palavra para maiúscula em uma coluna específica de um DataFrame
    data[col_name] = data[col_name].apply(lambda x: x.title())
    return data


def pre_processing(data):
    # Filtra todos os registros que não são vendas/cancelamento de produtos
    not_product_lines = data[data['StockCode'].apply(not_number)]

    # Remove do DataFrame os registros que não correspondem a vendas/cancelamentos de produtos
    not_product = not_product_lines['StockCode'].unique()
    data = data[~data['StockCode'].isin(not_product)]
    
    # Adiciona uma coluna de Preço Final de venda/devolução para cada transação
    data['FinalPrice'] = data['Quantity'] * data['UnitPrice']
    
    # Exclui os registros com valor unitário igual a zero
    data = data[data['UnitPrice'] > 0]
    
    # Remove as linhas duplicadas
    data = data.drop_duplicates()
    
    # Converte a primeira letra de cada palavra para maiúscula em uma coluna específica de um DataFrame
    title_col(data)
    
    return data


def change_types(data):
    # Ajusta os tipos de dados de algumas colunas em um DataFrame
    
    # Converte a coluna InvoiceDate para datetime com formato '%d/%m/%Y %H:%M'
    data['InvoiceDate'] = pd.to_datetime(data['InvoiceDate'], format='%d/%m/%Y %H:%M')
    
    # Converte a coluna CustomerID para string e remove qualquer ponto decimal
    data['CustomerID'] = data['CustomerID'].astype('str')
    data['CustomerID'] = data['CustomerID'].apply(lambda x: x.split('.')[0])
    
    # Converte a coluna Country para string
    data['Country'] = data['Country'].astype('str')
    
    return data


def drop_uk(data):
    # Remove todas as linhas onde o valor da coluna Country é 'United Kingdom'
    data = data.drop(data[data['Country'] == 'United Kingdom'].index)
    return data


def drop_nan(data, col_name='CustomerID'):
    # Remove todas as linhas onde o valor da coluna especificada é 'nan'
    data = data.drop(data[data[col_name] == 'nan'].index)
    return data


def add_time_columns(data):
    # Adiciona colunas relacionadas ao tempo baseadas na coluna InvoiceDate
    
    # Adiciona coluna com o nome do mês em português
    data['Month'] = data['InvoiceDate'].dt.month_name(locale='pt_BR')
    
    # Adiciona coluna com o nome do dia da semana em português
    data['Day'] = data['InvoiceDate'].dt.day_name(locale='pt_BR')
    
    # Adiciona coluna com o trimestre no formato 'T{n}'
    data['Quarter'] = data['InvoiceDate'].dt.quarter.apply(lambda x: f'T{x}')
    
    # Adiciona coluna com o ano
    data['Year'] = data['InvoiceDate'].dt.year
    
    return data


    




