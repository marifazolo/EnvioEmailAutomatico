#!/usr/bin/env python
# coding: utf-8

# In[9]:


import smtplib
import email.message

def enviar_email():
    corpo_email = """
    <p>Olá Mariana,</p>
    <p>Segue e-mail automático.</p>    
    """
    
    msg = email.message.Message()
    msg['Subject'] = 'E-mail Automático Python'
    msg['From'] = 'marianafazolo@gmail.com'
    msg['To'] = 'marianafazolo@gmail.com'
    password = 'bottbrkgwddvrxro'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)
    
    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    
    #Login
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('E-mail Enviado!')


# In[10]:


enviar_email()


# In[ ]:




