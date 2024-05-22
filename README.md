# Análise de Dados de E-Commerce

### Objetivo do Projeto
Este projeto tem como objetivo criar uma aplicação para analisar, sob diferentes aspectos, o conjunto de dados de E-Commerce de uma varejista online do Reino Unido. A aplicação foi desenvolvida para automatizar a análise dos dados, permitindo que sejam recebidos novos dados de outros períodos extraídos da mesma fonte e entregando análises sob diferentes perspectivas.

Essa aplicação espera facilitar e auxiliar na preparação de campanhas de vendas e marketing da empresa, além de contribuir para possíveis segmentações de produtos ou clientes, fornecendo um resumo rápido e interativo sobre os principais produtos, clientes, países compradores e sazonalidade das vendas dessa varejista.

### Motivação
O projeto foi realizado para aplicar os conhecimentos adquiridos em Python e análise de dados até o momento, após a conclusão da trilha de Python do DataCamp. O objetivo era treinar e colocar em prática diversos conceitos de desenvolvimento em Python, como módulos, pacotes e funções, aplicados à área de dados.


## Índice

- [Introdução](#introdução)

- [Fonte dos Dados](#fonte-dos-dados)

- [Dicionário dos Dados](#dicionário-dos-dados)

- [Análise Inicial do Dataset](#análise-inicial-do-dataset)

- [Estrutura do Projeto](#estrutura-do-projeto)

- [Funcionalidades](#funcionalidades)

- [Aprendizados](#aprendizados)

- [Executando Localmente](#executando-localmente)



## Introdução

Este conjunto de dados consiste em pedidos feitos em diferentes países de dezembro de 2010 a dezembro de 2011. A empresa é uma varejista online com sede no Reino Unido que vende principalmente presentes únicos para todas as ocasiões. Muitos de seus clientes são atacadistas.

## Fonte dos Dados

- **Citação**: Daqing Chen, Sai Liang Sain, and Kun Guo, Data mining for the online retail industry: A case study of RFM model-based customer segmentation using data mining, Journal of Database Marketing and Customer Strategy Management, Vol. 19, No. 3, pp. 197-208, 2012 (Publicado online antes da impressão: 27 de agosto de 2012. doi: 10.1057/dbm.2012.17)
- [Link](https://archive.ics.uci.edu/dataset/352/online+retail) do dataset
## Dicionário dos Dados
| Variável      | Explicação |
| ------------- | ---------- |
| InvoiceNo     | Número inteiro de 6 dígitos atribuído  a cada transação. Início com a letra 'C', indica um cancelamento. |
| StockCode     | Número inteiro de 5 dígitos atribuído  a cada produto distinto. |
| Description   | Nome do produto (item). |
| Quantity      | Quantidades de cada produto (item) por transação. |
| InvoiceDate   | Dia e hora em que cada transação foi gerada. |
| UnitPrice     | Preço do produto por unidade em libras esterlinas (pound). |
| CustomerID    | Número inteiro de 5 dígitos atribuído exclusivamente a cada cliente. |
| Country       | Nome do país onde cada cliente reside. |

## Análise Inicial do Dataset

Antes de desenvolver a aplicação, foi realizada uma análise inicial dos dados, documentada no arquivo **dataset_review.ipynb**.
A revisão do dataset foi muito importante para:

- Verificar duplicatas
- Verificar valores ausentes
- Verificar os tipos dos dados
- Identificar registros que não correspondiam a vendas/cancelamentos de produtos
- Outras inconsistências e peculiaridades dos dados

### Importância
A análise inicial foi fundamental para garantir a qualidade dos dados e a precisão das análises. A partir das descobertas feitas nesse estágio, foram criadas as funções de formatação e pré-processamento no arquivo **formatting.py**. 

Essas funções são responsáveis por limpar e preparar o dataset ao carregá-lo e também por formatar os dados de acordo com uma determinada análise escolhida pelo usuário. 

Para uma compreensão detalhada dos problemas encontrados e das soluções implementadas, recomenda-se a leitura do [documento de análise inicial](dataset_review.ipynb).
## Estrutura do Projeto
O projeto está organizado da seguinte forma:
- `Data/`: Contém o conjunto de dados de E-Commerce.
  - `Online Retail.csv`: O arquivo de dados principal.
- `functions/`: Contém as funções auxiliares.
  - `formatting.py`: Funções para formatação e pré processamento dos dados.
  - `functions.py`:  Funções de suporte.
- `menus/`: Contém o menu principal e submenus da aplicação.
  - `menus.py`: Definição dos menus.
- `results/`: Contém os scripts que geram as análises e resultados.
  - `clientes.py`: Análise dos clientes.
  - `paises.py`: Análise por país.
  - `produtos.py`: Análise dos produtos.
  - `sazonalidade.py`: Análise da sazonalidade.
- `app.ipynb`: Notebook principal da aplicação.
- `dataset_review.ipynb`: Notebook de análise inicial do dataset.
- `README.md`: Documentação do projeto.
## Funcionalidades


O programa oferece as seguintes opções de análise:

[1. Análise de Produtos](#1-análise-de-produtos)

[2. Análise de Clientes](#2-análise-de-clientes)

[3. Análise de Países](#3-análise-de-países)

[4. Análise de Sazonalidade](#4-análise-de-sazonalidade)

Cada uma dessas opções possui submenus com relatórios específicos.

### 1. Análise de Produtos

- *Produtos Mais Vendidos [Unidades]*: Exibe os produtos com **MAIOR SALDO** de vendas em termos de **UNIDADES**.

- *Produtos Mais Vendidos [Valor (£)]*:  Exibe os produtos com **MAIOR SALDO** de vendas em termos de **VALOR**.
- *Produtos Mais Vendidos [Ocorrências]*: Exibe os produtos **MAIS VENDIDOS** em termos de **OCORRÊNCIAS** de vendas.
- *Produtos Mais Cancelados [Unidades]*: Exibe os produtos **MAIS CANCELADOS** em termos de **UNIDADES**.
- *Produtos Mais Cancelados [Valor (£)]*: Exibe os produtos **MAIS CANCELADOS** em termos de **VALOR**.
- *Produtos Mais Cancelados [Ocorrências]*: Exibe os produtos mais cancelados em termos de **OCORRÊNCIAS** de cancelamentos.

#### Exemplo de Gráfico

Produtos Mais Vendidos [Unidades]:
![Produtos Mais Vendidos [Unidades]](images/produtos_mais_vendidos_unidades.png)

### 2. Análise de Clientes

- *Clientes Mais Compradores [Unidades]*: Exibe os clientes com **MAIOR SALDO** de compras em termos de **UNIDADES**.

- *Clientes Mais Compradores [Valor (£)]*: Exibe os clientes com **MAIOR SALDO** de compras em termos de **VALOR**.
- *Clientes Mais Compradores [Ocorrências]*: Exibe os clientes que **MAIS COMPRARAM** em termos de **OCORRÊNCIAS** de compras.
- *Clientes com Mais Cancelamento [Unidades]*: Exibe os clientes que **MAIS CANCELARAM** em termos de **UNIDADES**.
- *Clientes com Mais Cancelamento [Valor (£)]*: Exibe os clientes que **MAIS CANCELARAM** em termos de **VALOR**.
- *Clientes com Mais Cancelamento [Ocorrências]*: Exibe os clientes que **MAIS CANCELARAM** em termos de **OCORRÊNCIAS** de cancelamentos.

#### Exemplo de Gráfico

Clientes Mais Compradores [Unidades]:
![Clientes Mais Compradores [Unidades]](images/clientes_mais_compradores_unidades.png)

### 3. Análise de Países

- *Países Estrangeiros Mais Compradores [Unidades]*: Exibe os países estrangeiros com **MAIOR SALDO** de vendas em termos de **UNIDADES**.

- *Países Estrangeiros Mais Compradores [Valor (£)]*: Exibe os países estrangeiros com **MAIOR SALDO** de vendas em termos de **VALOR**.
- *Países Estrangeiros Mais Compradores [Ocorrências]*: Exibe os países estrangeiros que **MAIS COMPRARAM** em termos de **OCORRÊNCIAS** de compras.
- *Países Estrangeiros com Mais Cancelamentos [Unidades]*: Exibe os países estrangeiros que **MAIS CANCELARAM** em termos de **UNIDADES**.
- *Países Estrangeiros com Mais Cancelamentos [Valor (£)]*: Exibe os países estrangeiros que **MAIS CANCELARAM** em termos de **VALOR**.
- *Países Estrangeiros com Mais Cancelamentos [Ocorrências]*: Exibe os países estrangeiros que **MAIS CANCELARAM** em termos de **OCORRÊNCIAS** de cancelamentos.

#### Exemplo de Gráfico

Países Estrangeiros Mais Compradores [Unidades]:
![Países Estrangeiros Mais Compradores [Unidades]](images/paises_mais_compradores_unidades.png)

### 4. Análise de Sazonalidade

- *Variação Diária [Unidades]*: Exibe as vendas registradas por **DIA** em termos de **UNIDADES** vendidas.

- *Variação Diária [Valor (£)]*: Exibe as vendas registradas por **DIA** em termos de **VALOR** vendido.
- *Variação Diária [Ocorrências]*: Exibe as vendas registradas por **DIA** em termos de **OCORRÊNCIAS** de venda.
- *Variação Mensal [Unidades]*: Exibe as vendas registradas por **MÊS** em termos de **UNIDADES** vendidas.
- *Variação Mensal [Valor (£)]*: Exibe as vendas registradas por **MÊS** em termos de **VALOR** de vendido.
- *Variação Mensal [Ocorrências]*: Exibe as vendas registradas por **MÊS** em termos de **OCORRÊNCIAS** de venda.
- *Variação Trimestral [Unidades]*: Exibe as vendas registradas por **TRIMESTRE** em termos de **UNIDADES** vendidas.
- *Variação Trimestral [Valor (£)]*: Exibe as vendas registradas por **TRIMESTRE** em termos de **VALOR**s vendido.
- *Variação Trimestral [Ocorrências]*: Exibe as vendas registradas por **TRIMESTRE** em termos de **OCORRÊNCIAS** de venda.

#### Exemplo de Gráfico

Variação Diária [Unidades]:
![Variação Diária [Unidades]](images/variacao_diaria_unidades.png)
## Executando Localmente

Certifique-se de ter os seguintes itens instalados em sua máquina:

- Python 3.7 ou superior
- Jupyter Notebook
- Pandas
- Numpy
- Matplotlib
- Seaborn

### Passo a Passo

**1.** Clone o repositório para sua máquina local\
**2.** Navegue até o diretório\
**3.** Inicie o Jupyter Notebook\
**4.** Abra o arquivo app.ipynb no Jupyter Notebook\
**5.** Execute a célula no app.ipynb contendo a função main

### Notas Adicionais

- Certifique-se de que os arquivos de dados estejam presentes na pasta Data/ conforme a estrutura do projeto.
- Siga as instruções e execute as células do notebook para rodar a aplicação. Você verá as opções de análise disponíveis e poderá interagir com a aplicação diretamente no notebook.

## Aprendizados

O desenvolvimento deste projeto proporcionou a aplicação prática de diversas áreas de conhecimento em análise de dados e programação em Python. A modularização e documentação do projeto aprimoraram as boas práticas de codificação. Além disso, foram utilizados conhecimentos em manipulação de grandes volumes de dados, incluindo pré-processamento, limpeza e transformação de dados com a biblioteca Pandas. Por fim, também foram aplicadas técnicas de visualização de dados, com a construção de gráficos e tabelas com Seaborn e Matplotlib.
## Autor

- [@matheusbnc](https://github.com/matheusbnc)

