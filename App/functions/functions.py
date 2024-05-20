import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

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
    ax = sns.barplot(data=data.head(15), 
                             x=x_axes, y= y_axes, 
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
    
def plot_line(data):
    pass





