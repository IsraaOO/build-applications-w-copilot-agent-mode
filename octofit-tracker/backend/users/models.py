from django.db import models


class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    weight = models.FloatField()
    height = models.FloatField()

    def __str__(self):
        return self.username