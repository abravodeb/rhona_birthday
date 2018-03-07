from django.db import models
import datetime

# Create your models here.

class Mensaje(models.Model):
    msg = models.TextField(max_length=400)
    def __str__(self):
        return self.msg

class Cumple(models.Model):
    nombre = models.CharField(blank=False, max_length=150)
    mail = models.EmailField(max_length=254)
    msg = models.ForeignKey(Mensaje)
    cumple = models.DateTimeField(default=datetime.datetime.today)

    def __str__(self):
        return "%s | %s" %(self.nombre, self.cumple)