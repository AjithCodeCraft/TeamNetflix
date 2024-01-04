from django.db import models

from django.db import models

class Register(models.Model):
    username = models.CharField(max_length=255, unique=True)
    fullname = models.CharField(max_length=122)
    email = models.EmailField(unique=True)
    phno = models.CharField(max_length=12,unique=True)
    password = models.CharField(max_length=255)
    registration_date = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.username