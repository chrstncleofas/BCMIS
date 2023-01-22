from django.db import models

# Create your models here.
class Resident(models.Model):
    name = models.CharField(max_length=70)
    birthday = models.CharField(max_length=70)
    email = models.CharField(max_length=70)
    phone = models.CharField(max_length=70)
    address = models.CharField(max_length=70)
    age = models.CharField(max_length=70)
    status = models.CharField(max_length=70)
    citizen = models.CharField(max_length=70)
    gender = models.CharField(max_length=70)
    id_type = models.CharField(max_length=70)
    id_no = models.CharField(max_length=70)
    member = models.CharField(max_length=70)

    def __str__(self):
        return f'Resident: {self.name}'