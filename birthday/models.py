from django.db import models
import datetime

# Create your models here.

class birthday_message(models.Model):
    msg = models.TextField(max_length=400, verbose_name="Mensaje")

    class Meta:
        verbose_name="Mensaje de cumpleaño"
        verbose_name_plural ="Mensajes de cumpleaños"

    def __str__(self):
        return self.msg

class birthday_day(models.Model):
    name = models.CharField(blank=False, max_length=150, verbose_name="Nombre")
    email = models.EmailField(max_length=254, verbose_name="e-mail")
    msg = models.ForeignKey(birthday_message, verbose_name="Mensaje")
    bday = models.DateTimeField(default=datetime.datetime.today, verbose_name="Fecha de cumpleaño")

    class Meta:
        verbose_name="Registro de cumpleaño"
        verbose_name_plural ="Registros de cumpleaños"

    def __str__(self):
        return "%s | %s" %(self.name, self.bday)