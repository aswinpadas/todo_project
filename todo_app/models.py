from django.db import models

# Create your models here.
from pyexpat import model


class Task(models.Model):
    def __str__(self):
        return self.name
    name=models.CharField(max_length=100)
    priority=models.IntegerField()
    def setTask(self,name,priority):
        self.name=name
        self.priority=priority
