import smtplib 
import os 
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from decouple import config

# environ var from .env
email = config('USERNAME_MAIL')
password = config('USERNAME_MAIL_PASSWORD')

body = """\
<html>
  <head></head>
  <body>
    <p>Hi!<br>
    <p> <h2> %s </h2> </p>
       Estimado %s, te deseamos un feliz cumpleanos<br>
       Visita el link <a href="http://www.rhona.cl">rhona</a>.
    </p>
    <img src="http://165.227.198.116/rhona/saludos-cumple.jpg">
    <p>
    Este email fue generado automaticamente, by kainsaateam
    </p>
  </body>
</html>
"""

def send_email(name,mail,message1):
      name = name
      message = message1
      to_address = mail
      smtp_obj = smtplib.SMTP('smtp.gmail.com',587)
      smtp_obj.starttls()
      part2 = MIMEText(body, 'html')
      mess = MIMEMultipart('alternative')
      mess.attach(part2)
      print(smtp_obj.login(email,password))
      from_addres = 'Comunicaciones kainsaa' # check var
      subject = "Felicitaciones %s" % (name)
      msg = "Subject: " + subject + "\n" + mess.as_string() % (name,message) 
      smtp_obj.sendmail(from_addres,to_address,msg)
      smtp_obj.quit()
      print("send email...")