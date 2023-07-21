from django.contrib import admin
from .models import Personnel, Contacts


class PersonnelAdmin(admin.ModelAdmin):
    search_fields = ['service_number', 'last_name', 'rank',]

class ContactsAdmnin(admin.ModelAdmin):
    search_fields = ['phone_number']


# Register your models here.
admin.site.register(Personnel, PersonnelAdmin)
admin.site.register(Contacts, ContactsAdmnin)