def main_menu():
    # Exibe o menu principal com as opções de análise
    print('='*80)
    print('MENU PRINCIPAL'.center(80))
    print('='*80)
    print('1. Análise de Produtos')
    print('2. Análise de Clientes')
    print('3. Análise de Países')
    print('4. Análise de Sazonalidade')
    print('='*80)
    print('0. Sair')    

def produto_submenu():
    # Exibe o submenu de análise de produtos com várias opções de relatórios
    print('\n' + '='*80)
    print('ANÁLISE DE PRODUTOS'.center(80))
    print('='*80)
    print('1. Produtos Mais Vendidos [Unidades]')
    print('2. Produtos Mais Vendidos [Valor (£)]')
    print('3. Produtos Mais Vendidos [Ocorrências]')
    print('4. Produtos Mais Cancelados [Unidades]')
    print('5. Produtos Mais Cancelados [Valor (£)]')
    print('6. Produtos Mais Cancelados [Ocorrências]')
    print('='*80)
    print('0. Voltar ao Menu Principal')

def cliente_submenu():
    # Exibe o submenu de análise de clientes com várias opções de relatórios
    print('\n' + '='*80)
    print('ANÁLISE DE CLIENTES'.center(80))
    print('='*80)
    print('1. Clientes Mais Compradores [Unidades]')
    print('2. Clientes Mais Compradores [Valor (£)]')
    print('3. Clientes Mais Compradores [Ocorrências]')
    print('4. Clientes com Mais Cancelamento [Unidades]')
    print('5. Clientes com Mais Cancelamento [Valor (£)]')
    print('6. Clientes com Mais Cancelamento [Ocorrências]')
    print('='*80)
    print('0. Voltar ao Menu Principal')

def pais_submenu():
    # Exibe o submenu de análise de países com várias opções de relatórios
    print('\n' + '='*80)
    print('ANÁLISE DE PAÍSES'.center(80))
    print('='*80)
    print('1. Países Estrangeiros Mais Compradores [Unidades]')
    print('2. Países Estrangeiros Mais Compradores [Valor (£)]')
    print('3. Países Estrangeiros Mais Compradores [Ocorrências]')
    print('4. Países Estrangeiros com Mais Cancelamentos [Unidades]')
    print('5. Países Estrangeiros com Mais Cancelamentos [Valor (£)]')
    print('6. Países Estrangeiros com Mais Cancelamentos [Ocorrências]')
    print('='*80)
    print('0. Voltar ao Menu Principal')

def sazonalidade_submenu():
    # Exibe o submenu de análise de sazonalidade com várias opções de relatórios
    print('\n' + '='*80)
    print('ANÁLISE DE SAZONALIDADE'.center(80))
    print('='*80)
    print('1. Variação de Vendas/Cancelamentos [Dias]')
    print('2. Variação de Vendas/Cancelamentos [Meses]')
    print('3. Variação de Vendas/Cancelamentos [Trimestres]')
    print('='*80)
    print('0. Voltar ao Menu Principal')
