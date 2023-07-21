from typing import Any
from django.db import models

# Create your models here.

#Personel model for DB
class Personnel(models.Model):
    service_number = models.IntegerField(unique=True, null=False, primary_key=True, blank=False)
    file_number = models.IntegerField(unique=True, null=False, blank=False)
    first_name = models.CharField(max_length=100, null=False, blank=False)
    middle_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    sex = models.CharField(max_length=10, null=False, blank=False)
    rank = models.CharField(max_length=10, null=False, blank=False)

    def __str__(self):
        return f"{self.rank} - {self.first_name} {self.last_name}"
    
#custom function to validate phone number 
def validate_phone_number_length(value):
    if len(value) != 11:
        raise ValueError('Phone Number have 11 digit')

#contact model for DB
class Contacts(models.Model):
    service_number = models.ForeignKey(Personnel, on_delete=models.CASCADE)
    State_of_origin = models.CharField(max_length=100, null=False, blank=False)
    local_gov_area = models.CharField(max_length=100, null=False, blank=False)
    phone_number = models.CharField(max_length=11, null=True, blank=True, validators=[validate_phone_number_length])

    def __str__(self) -> str:
        return f"{self.service_number} - {self.phone_number}"
    
