from django.db import models

# Create your models here.


class Tracker_model(models.Model):
    Date=models.DateField()
    Description=models.CharField(max_length=60)
    Amount=models.IntegerField()
    category=models.CharField(max_length=20)
