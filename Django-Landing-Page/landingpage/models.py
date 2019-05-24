from django.db import models

class CustomerData(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    npo = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    month = models.CharField(max_length=255)

    def __str__(self):
        return self.npo
