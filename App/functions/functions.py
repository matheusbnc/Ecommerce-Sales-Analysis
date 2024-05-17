#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
# Configurando o estilo de plotagem do seaborn
sns.set_style('whitegrid')


# In[2]:

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


def pre_processing(sales):
    # Filtra todos os registros que não vendas/cancelamento de produtos
    not_product_lines = sales[sales['StockCode'].apply(not_number)]

    # Obter os valores únicos das linhas
    not_product = not_product_lines['StockCode'].unique()
    
    sales = sales[~sales['StockCode'].isin(not_product)]
    
    # Adicionando coluna de Preço Final de venda/devolução para cada transação
    sales['FinalPrice'] = sales['Quantity'] * sales['UnitPrice']
    
    # Excluindo os registros com valor unitário igual a zero
    sales = sales[sales['UnitPrice'] > 0]
    
    # Remove as linhas duplicadas 
    sales = sales.drop_duplicates()
    
    # Converte a primeira letra de cada palavra para maíuscula em uma coluna específica de um dataframe
    title_col(sales)
    
    return sales

def change_types(sales):
    sales['InvoiceDate'] = pd.to_datetime(sales['InvoiceDate'], format = '%d/%m/%Y %H:%M').dt.date
    sales['CustomerID'] = sales['CustomerID'].astype('str')
    sales['CustomerID'] = sales['CustomerID'].apply(lambda x: x.split('.')[0])
    sales['Country'] = sales['Country'].astype('str')

def drop_nan(data, col_name='CustomerID'):
    data = data.drop(data[data['CustomerID'] == 'nan'].index)
    return data

def format_number(num):
    '''
    Formata o número de acordo com o tipo de número recebido
    
    Parâmetro:
        num (int, float): Número a ser formatado
    '''
    if isinstance(num, float):
        if num.is_integer(): # Checa se a parte fracionária do float é zero
            return f"{int(num):d}"  # Transforma o float para int
        else:
            return f"{num:.2f}" # Retorna o float com 2 casas decimais
    if isinstance(num, int):
        return f"{num:d}"  # Retorna o número inteiro normalmente
    if isinstance(num, str):
        return str(num)
    else:
        return str(num)  # Retorna como string se não for int. float ou string


# In[3]:


def add_bar_values(ax, space=5):
    '''
    Imprime os valores exatos de cada barra em um gráfico de barras horizontal
    
    Parâmetros:
        ax (matplotlib.axes.Axes): Gráfico a ser personalizado
        space (int, opcional): Espaçamento entre a barra e o início do texto. Padrão: 3
    '''
    for i in ax.patches: 
        bar_value = i.get_width() # Obtém o valor correspondente da barra, representado pela largura
        ax.text(bar_value + space, # Determina a posição horizontal de onde o valor será impresso
                i.get_y() + i.get_height() / 2, # Determina a posição vertical de onde o valor será impresso
                format_number(bar_value), # Valor que será impresso (formatado)
                ha='left', # Alinhamento horizontal do texto a esquerda
                va='center', # Alinhamento vertical do texto centralizado 
                fontsize=10) # Tamanho da fonte do número


# In[4]:


def plot_bar(data, x_axes, y_axes, x_label, y_label, title, palette='viridis', space=5):
    plt.figure(figsize=(13,9))
    ax = sns.barplot(data=data.head(15), 
                             x=x_axes, y= y_axes, 
                             palette=palette)
    plt.xlabel(x_label, fontsize=14, fontweight='bold')
    plt.ylabel(y_label, fontsize=14, fontweight='bold')
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.title(title, fontsize=16, fontweight='bold')
    add_bar_values(ax, space)
    plt.show()
 

# In[ ]:




