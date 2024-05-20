#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
from functions.functions import plot_line, data_summary
from time import sleep


# In[ ]:


def daily_variation_quantity(sales_saz):
    sales_saz = sales_saz.groupby('Day').apply(lambda x: pd.Series({
        'Quantidade Vendida': x.loc[~x['InvoiceNo'].str.startswith('C'), 'Quantity'].sum()\
        ,'Quantidade Cancelada': x.loc[x['InvoiceNo'].str.startswith('C'), 'Quantity']\
        .sum()})).reset_index()
    sales_saz['Quantidade Cancelada'] = sales_saz['Quantidade Cancelada'].abs()
    # Converter a coluna 'Day' para uma categoria para manter a ordem correta dos dias
    salez_saz['Day'] = pd.Categorical(df['Day'], categories=['Domingo', 'Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira'], ordered=True)
    data_summary(sales_saz)    


# In[ ]:




