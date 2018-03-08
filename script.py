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
from birthday.models import BirthdayDay

# get current day & month
currentDay = datetime.now().day
currentMonth = datetime.now().month

# test, print all users
def get_all_users():
    users = BirthdayDay.objects.all()
    # test
    for i in users:
        print(i.id)
        print(i.name)
        print(i.msg)
        print(i.birthday_day)

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
    total_users = BirthdayDay.objects.all()
    print("Number of users:", len(total_users))
    cumples = BirthdayDay.objects.filter(birthday_day__month=currentMonth,birthday_day__day=currentDay) # filter
    return cumples

if __name__ == '__main__':
    #get_all_users()
    cumple = query_today()
    for i in cumple:
        print(i.name)
    print("User filter by date : ", len(cumple))
    for i in cumple:
        test_image_name(i.name,"Regards...")
        send_email(i.name,i.mail,i.msg)

