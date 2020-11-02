from django.db import models

class user(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=200)
    password=models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

