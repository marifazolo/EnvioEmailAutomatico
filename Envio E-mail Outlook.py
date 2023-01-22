#!/usr/bin/env python
# coding: utf-8

# In[36]:


import win32com.client as win32
outlook = win32.Dispatch('outlook.application')
import pandas as pd


# In[40]:


base_dados = pd.read_excel(r'Base de Dados.xlsx')
display(base_dados)

for i, email in enumerate(base_dados):

    Codcliente = base_dados.loc[i, 'Cód Cliente']
    Nome = base_dados.loc[i, 'Nome']
    Email = base_dados.loc[i, 'E-mail']
    Oferta = base_dados.loc[i, 'Oferta']
    Qtdcotas = base_dados.loc[i, 'Qtde Cotas']
    Valorcota = base_dados.loc[i, 'Valor Cota']
    Financeiro = base_dados.loc[i, 'Financeiro']
    
    mail = outlook.CreateItem(0)
    mail.To = Email
    mail.Subject = Oferta
    mail.Body = ''' {}, boa tarde!

Gostaria de confirmar a reserva de compra no seu código {}:

Oferta: {}
Quantidade de Cotas: {}
Valor da Cota: R$ {:.2f}
Valor Financeiro Total: R$ {:,.2f}
    
Aguardo sua confirmação.
'''.format(Nome, Codcliente, Oferta, Qtdcotas, Valorcota, Financeiro)
    
    mail.Send()

