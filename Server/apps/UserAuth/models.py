from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=255)

    class Meta:
        db_table = "User"


class AdminUser(models.Model):
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=255)
    login_date = models.DateTimeField()

    class Meta:
        db_table = "AdminUser"
