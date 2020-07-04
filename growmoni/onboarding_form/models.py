from django.db import models

# Create your models here.


class Clients(models.Model):
    name = models.CharField("Name", max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    business_name = models.CharField(max_length=150)
    country = models.CharField(max_length=30)

    def __str__(self):
        return self.name
