from django.db import models

# Create your models here.
class Student(models.Model):
  name=models.CharField(max_length=20)
  inclass = models.CharField(max_length=20)
  image=models.ImageField(null=True,blank=True,upload_to='images/') 
  video= models.FileField(null=True,blank=True,upload_to='videos/') 

class Books(models.Model):
  name=models.CharField(max_length=50)
  author=models.CharField(max_length=50)
  publications=models.CharField(max_length=30)
  year=models.DateTimeField(null=True,blank=True)

class Library(models.Model):
  studentname=models.CharField(max_length=20)
  bookname=models.CharField(max_length=20)
  starteddate=models.DateField(null=True)
  endedate=models.DateField(null=True)
