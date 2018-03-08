import os
import django
from faker import Faker
from random import randint

# Generates random users - name, date entries for testing. 

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rhona.settings")
django.setup()

import random
from birthday.models import BirthdayDay,BirthdayMessage

fakegen = Faker()

def insert_users(N=40):
    for i in range(N):
        msg = BirthdayMessage.objects.first()
        fake_name = fakegen.name()
        # fake_msg = randint(1, 3)
        fake_cumple = fakegen.date_time()

        c = BirthdayDay.objects.create(name=fake_name,msg=msg,birthday_day=fake_cumple)
        c.save()

# generate 100 random users.
insert_users(100)
