import datetime

from django.db import models

# Create your models here.
from pyexpat import model


class Task(models.Model):
    def __str__(self):
        return self.name
    name=models.CharField(max_length=100)
    priority=models.IntegerField()
    date= models.DateField()
    completed=models.BooleanField(default=False)
    image=models.ImageField(upload_to='images/',default='images/None/Noimg.jpg')
    def setTask(self,name,priority,date):
        self.name=name
        self.priority=priority
        self.date=date
