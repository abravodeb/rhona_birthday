import os
import django
from faker import Faker
from random import randint

# script para poblar base de datos

### 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rhona.settings")
django.setup()

import random
from birthday.models import *

fakegen = Faker()

#print(fakegen.name(), fakegen.date_time())

# print(randint(0, 9))

def insert_users(N=40):
    for i in range(N):
        msg = Mensaje.objects.first()
        fake_name = fakegen.name()
        # fake_msg = randint(1, 3)
        fake_cumple = fakegen.date_time()

        c = Cumple.objects.create(nombre=fake_name,msg=msg,cumple=fake_cumple)
        c.save()

insert_users(100)
