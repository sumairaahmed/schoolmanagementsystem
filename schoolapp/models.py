from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Student(models.Model):
    user = models.OneToOneField(User, null=True ,on_delete=models.CASCADE)
    profile_pic = models.FileField(default='default.jpg',upload_to='profile_pics')
    age = models.IntegerField(null=True,blank=True)
    address = models.TextField()
    clas = models.CharField(max_length=10)
    phone = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Student.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.student.save()

class Teacher(models.Model):
    profile_pic = models.FileField(upload_to='profile_pic',default='default.jpg')
    username = models.CharField(max_length=50)
    name = models.CharField(max_length=50, null=True,blank=True)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    phone = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return self.username

class notes(models.Model):
    subject = models.CharField(max_length=200)
    module = models.IntegerField()
    notess = models.FileField(upload_to='pdfs')
    def __str__(self):
        return self.subject
# Create your models here.
