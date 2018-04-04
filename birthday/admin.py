from django.contrib import admin
from .models import birthday_day, birthday_message
# Register your models here.

class birthdayMessageAdmin(admin.ModelAdmin):
    search_fields = ['msg']
    list_fields = ['msg']
    filter_fields = ['msg']

admin.site.register(birthday_message, birthdayMessageAdmin)

class birthdayDayAdmin(admin.ModelAdmin):
    search_fields = ['name','bday','email']
    list_filter = ['bday']
    list_display = ['name','bday','email']

admin.site.register(birthday_day, birthdayDayAdmin)