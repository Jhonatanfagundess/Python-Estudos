from email.message import EmailMessage
import smtplib
import ssl

password = open('senha', 'r').read()
from_email = 'jhonatanfagundec15@gmail.com'
to_email = 'jhonatanfagundec17@yahoo.com.br'
subject = 'Curso de Burro'
body = """
Nosso estudo em Python é complicado mas estamos dando o que podemos dar!!
"""
# Estrutuda da mensagem via email
messange = EmailMessage()
messange['From'] = from_email
messange['To'] = to_email
messange['Subject'] = subject
messange.set_content(body)
safe = ssl.create_default_context()

#Envio de email
with smtplib.SMTP_SSL('smtp.gmail.com', 465 , context=safe) as smtp:
    smtp.login(from_email,password)
    smtp.sendmail(
        from_email,
        to_email,
        messange.as_string()
    )