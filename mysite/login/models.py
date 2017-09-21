from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=100, verbose_name='username')
    email = models.EmailField(verbose_name='e-mail')
    password = models.CharField(max_length=40, verbose_name='password')
    c_password = models.CharField(max_length=40, verbose_name='confirm password')
    
    def __str__(self):
        return self.username

    class Meta: 
        ordering = ['username']


