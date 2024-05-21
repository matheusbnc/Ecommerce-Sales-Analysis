import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
from matplotlib.ticker import ScalarFormatter

# Configurando o estilo de plotagem do seaborn
sns.set_style('whitegrid')


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
                fontsize=12) # Tamanho da fonte do número

def plot_bar(data, x_axes, y_axes, x_label, y_label, title, palette='viridis', space=5):
    plt.figure(figsize=(13,9))
    ax = sns.barplot(data= data.head(15), 
                             x=x_axes, y=y_axes, 
                             palette=palette)
    plt.xlabel(x_label, fontsize=14, fontweight='bold')
    plt.ylabel(y_label, fontsize=14, fontweight='bold')
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.title(title, fontsize=16, fontweight='bold')
    add_bar_values(ax, space)
    plt.tight_layout()
    plt.show()

def data_summary(sales):
    print('RESUMO DOS DADOS'.center(120))
    print("="*120)
    print(sales.head(15))
    print("="*120)
    

def plot_line(data1, data2, x_axes, y_axes, x_label, y_label, title1, title2, rotation=45):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

    sns.lineplot(data=data1, x=x_axes, y=y_axes, ax=ax1, marker='o', color='green')
    ax1.set_title(title1, fontsize=16, fontweight='bold')
    ax1.set_xlabel(x_label, fontsize=14, fontweight='bold')
    ax1.set_ylabel(y_label, fontsize=14, fontweight='bold')
    ax1.tick_params(axis='x', labelsize=12, rotation=rotation)
    ax1.tick_params(axis='y', labelsize=12)
    ax1.grid(True, linestyle='--', alpha=0.6)
    ax1.margins(x=0.01)
    ax1.yaxis.set_major_formatter(ScalarFormatter(useOffset=False, useMathText=False))
    ax1.yaxis.get_major_formatter().set_scientific(False)

    sns.lineplot(data=data2, x=x_axes, y=y_axes, ax=ax2, marker='o', color='red')
    ax2.set_title(title2, fontsize=16, fontweight='bold')
    ax2.set_xlabel(x_label, fontsize=14, fontweight='bold')
    ax2.set_ylabel('')
    ax2.tick_params(axis='x', labelsize=12, rotation=rotation)
    ax2.tick_params(axis='y', labelsize=12)
    ax2.grid(True, linestyle='--', alpha=0.6)
    ax2.margins(x=0.01)
    
    plt.tight_layout()
    plt.show()


    
def group_data(data, group_col='Description', operation_col='Quantity', operation='sum', how='balance'):
    
    if how == 'balance':
        data = data.groupby(group_col).agg({operation_col : operation}).reset_index()
        
    elif how == 'sales':
        data = data[~data['InvoiceNo'].str.startswith('C')].groupby(group_col)\
                        .agg({operation_col : operation}).abs().reset_index()
    elif how == 'cancellations':
        data = data[data['InvoiceNo'].str.startswith('C')].groupby(group_col)\
                        .agg({operation_col : operation}).abs().reset_index()
    else:
        raise ValueError("Argumento 'how' deve ser 'balance', 'sales' ou 'cancellations'.")

    data = data.sort_values(by=[operation_col], ascending=False).reset_index(drop=True)    
    
    return data
    

def order_days(data):
    data['Day'] = pd.Categorical(data['Day'],
                                 categories=['Domingo', 'Segunda-feira', 'Terça-feira',\
                                             'Quarta-feira', 'Quinta-feira', 'Sexta-feira'],
                                 ordered=True)
    return data.sort_values(by=['Day']).reset_index(drop=True)

def order_months(data):
    data['Month'] = pd.Categorical(data['Month'],
                                 categories=['Janeiro', 'Fevereiro', 'Março',\
                                             'Abril', 'Maio', 'Junho',\
                                             'Julho', 'Agosto', 'Setembro',\
                                             'Outubro', 'Novembro', 'Dezembro'],
                                 ordered=True)
    return data.sort_values(by=['Month']).reset_index(drop=True)


def order_quarters(data):
    data['Quarter'] = pd.Categorical(data['Quarter']\
                            ,categories=['T1', 'T2', 'T3', 'T4'], ordered=True)
    
    return data.sort_values(by=['Quarter']).reset_index(drop=True)