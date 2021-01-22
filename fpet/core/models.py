from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Pet(models.Model):
    city = models.CharField(max_length = 100)
    district = models.CharField(max_length = 100)
    description = models.TextField()
    breed = models.CharField(max_length = 100)
    email = models.EmailField()
    begin_date = models.DateTimeField(auto_now_add = True)
    phone = models.CharField(max_length=11, null=True)
    photo = models.ImageField(upload_to='pet', blank=True, null=True)
    active = models.BooleanField(default = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'pet'


class Euvi(models.Model): #dados do usuario que viu o pet
    city = models.CharField(max_length = 100)
    district = models.CharField(max_length = 100)
    email = models.EmailField()
    phone = models.CharField(max_length=11, null=True)
    active = models.BooleanField(default = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    photo = models.ImageField(upload_to='euvi', blank=True, null=True)
    begin_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'euvi'
