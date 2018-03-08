from django.contrib import admin
from .models import BirthdayDay, BirthdayMessage
# Register your models here.

class MessageAdmin(admin.ModelAdmin):
    search_fields = ['msg']
    list_fields = ['msg']
    filter_fields = ['msg']

admin.site.register(BirthdayMessage,MessageAdmin)


class BirthdayDayAdmin(admin.ModelAdmin):
    search_fields = ['name','birthday_day','mail']
    list_filter = ['birthday_day']
    list_display = ['name','birthday_day','mail']


admin.site.register(BirthdayDay,BirthdayDayAdmin)