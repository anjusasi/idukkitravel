from django.db import models


# Create your models here.



# class Book(models.Model):
#     name=models.CharField(max_length=230)
#     age=models.IntegerField()
#     email=models.EmailField()
#     phone=models.CharField(max_length=12)
#     where_to=models.TextField()
#     how_many=models.IntegerField()
#     arrivals=models.DateField()
#     leaving=models.DateField()
#
#
#     def __str__(self):
#         return self.name

class Package(models.Model):
    img = models.ImageField(upload_to='pics')
    locname = models.CharField(max_length=250)
    desc = models.TextField()

    def __str__(self):
        return self.locname