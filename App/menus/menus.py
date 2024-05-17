def main_menu():
    print("Menu Principal:")
    print("1. Análise de Produtos")
    print("2. Análise de Clientes")
    print("3. Análise de Países")
    print("4. Análise de Sazonalidade")
    print("0. Sair")

def produto_submenu():
    print("\nAnálise de Produtos:")
    print("1. Quais são os 15 produtos mais vendidos em termos de quantidade no período?")
    print("2. Quais são os 15 produtos mais vendidos em termos de receita no período?")
    print("3. Quais são os 15 produtos com mais ocorrências de compra no período?")
    print("4. Quais são os 15 produtos mais cancelados em termos de quantidade no período?")
    print("5. Quais são os 15 produtos mais cancelados em termos de receita no período?")
    print("6. Quais são os 15 produtos com mais ocorrências de cancelamento no período?")
    print("0. Voltar ao Menu Principal")

def cliente_submenu():
    print("\nAnálise de Clientes:")
    print("1. Quais são os 15 clientes com mais unidades compradas no período?")
    print("2. Quais são os 15 clientes com maior valor gasto no período?")
    print("3. Quais são os 15 clientes com mais ocorrências de compra no período?")
    print("4. Quais são os 15 clientes com mais unidades canceladas no período?")
    print("5. Quais são os 15 clientes com maior valor cancelado no período?")
    print("6. Quais são os 15 clientes com maior ocorrências de cancelamento no período?")
    print("0. Voltar ao Menu Principal")

def pais_submenu():
    print("\nAnálise de Países:")
    print("1. Quais são os países com os maiores volumes de vendas no período?")
    print("2. Quais são os países que mais geraram receita no período?")
    print("3. Quais são os países com mais ocorrências de cancelamento no período?")
    print("4. Quais são os países com maior valor médio de compra por transação no período?")
    print("0. Voltar ao Menu Principal")

def sazonalidade_submenu():
    print("\nAnálise de Sazonalidade:")
    print("1. Como a quantidade de vendas varia ao longo dos dias da semana para cada ano?")
    print("2. Como a quantidade de vendas varia ao longo dos trimestres para cada ano?")
    print("3. Como a quantidade de vendas varia ao longo dos meses para cada ano?")
    print("0. Voltar ao Menu Principal")
