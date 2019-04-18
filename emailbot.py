import smtplib, ssl
import getpass
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import destinatario
import mimetypes
from email.mime.image import MIMEImage
import endr
lista = destinatario.lista
tam = len (lista)
env = endr.end
senha = getpass.getpass("senha: ")
mensagem = MIMEMultipart("alternative")
mensagem["Subject"] = "CONHEÇA MEU NOVO SITE"
mensagem["From"] = env

text = """\
"""
html = """\
<html>
<body>
<p>
<br><br>
OLÁ ACESSE E CONHEÇA MEU NOVO SITE -->>> <a href ="https://bitblender.000webhostapp.com/">LINK AQUI</a>
<br> OBRG. <br><br>
MIXAGEM DE BITCOINS ------>TESTE MEU SISTEMA <a href="https://7bitblender.000webhostapp.com/">AQUI</a> OU ENTRE EM CONTATO PARA SABER MAIS.
<br>
OUTROS CONTATOS:<b>
TELEGRAM: <a href="">@biwxx</a>
</P>  

</body>
</html>
"""
def anexa(msg, filename):
    with open(filename, 'rb') as f:
        mime = MIMEImage(f.read(), _subtype='jpg')
     
    mime.add_header('Content-Disposition', 'attachment', filename=filename)
    mensagem.attach(mime)
    encoders.encode_base64(mime)

part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")
mensagem.attach(part1)
mensagem.attach(part2)
anexa(mensagem, 'Captura de tela_2019-04-16_15-39-30.jpg')


for i in range(tam):
    x= destinatario.lista[i]
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(env,senha)
        server.sendmail(
            env, x, mensagem.as_string()
    )

print ("ENVIADO!\n")

