from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Business_centres(models.Model):
    centre_name = models.CharField(max_length=20)
    contact_info = models.CharField(max_length=20)
    emergency_service = models.BooleanField(default=False)

    def __str__(self):
        return self.centre_name

    def save_centre(self):
        self.save()

    def delete_centre(self):
        self.delete()

class Neighbourhood(models.Model):
    Name = models.CharField(max_length=20)
    Centres = models.ManyToManyField(Business_centres)

    def __str__(self):
        return self.name

    def save_Neighbourhood(self):
        self.save()

    def delete_Neighbourhood(self):
        self.delete()

class Profile(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    Location = models.CharField(max_length=50)
    user_avatar = models.ImageField(upload_to = 'images/')
    Neighbourhood =  models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)

    def __str__(self):
        return self.username.username

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    class Meta:
        ordering = ['username']
