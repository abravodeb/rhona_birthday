import os
import django
import faker

# Generates random users - name, date entries for testing.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rhona.settings")
django.setup()

import random
import birthday.models
fakegen = faker.Faker()

def insert_users(N=40):
    for i in range(N):
        msg = birthday.models.birthday_message.objects.first()
        fake_name = fakegen.name()
        fake_cumple = fakegen.date_time()
        c = birthday.models.birthday_day.objects.create(name=fake_name, msg=msg, bday=fake_cumple)
        c.save()

# generate 100 random users.
insert_users(100)
