# -*- coding: utf-8 -*-
import os
import django
from django.utils import timezone
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from send_gmail_email import send_email

#today = date.today() # 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rhona.settings")
django.setup()

# import birthday model 
from birthday.models import Cumple

# get current day & month
currentDay = datetime.now().day
currentMonth = datetime.now().month

# test, print all users
def get_all_users():
    users = Cumple.objects.all()
    # test
    for i in users:
        print(i.id)
        print(i.nombre)
        print(i.msg)
        print(i.cumple)

# test - add text on image

def test_image_name(name, msg):
    image = Image.open('static/saludo_test.jpg')
    font_type = ImageFont.truetype('static/fonts/Mossy.ttf', 35)
    draw = ImageDraw.Draw(image)
    draw.text(xy=(300, 400),text=msg,fill=(27,80,25),font=font_type)
    draw.text(xy=(65, 400),text=name,fill=(27,80,25),font=font_type)
    image.show()

# get all users and filter by date.
def query_today():
    total_users = Cumple.objects.all()
    print("usuarios totales en BD:", len(total_users))
    cumples = Cumple.objects.filter(cumple__month=currentMonth,cumple__day=currentDay) # filter
    return cumples

if __name__ == '__main__':
    #get_all_users()
    print("pruebas con filtro, fecha de hoy!  ---- ")
    cumple = query_today()
    for i in cumple:
        print(i.nombre)
    print("Usuarios Filtrados por fecha: ", len(cumple))
    for i in cumple:
        test_image_name(i.nombre,"saludos...")
        send_email(i.nombre,i.mail,i.msg)

