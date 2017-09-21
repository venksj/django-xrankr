from django.db import models

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(verbose_name='e-mail')
    
    def __str__(self):
        return u'%s %s' %(self.first_name, self.last_name)

    class Meta: 
        ordering = ['first_name']


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30, verbose_name='state')
    country = models.CharField(max_length=50)
    website = models.URLField()

    def __str__(self):
        return u'%s, %s' %(self.name, self.city)

    class Meta: 
        ordering = ['name']

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField(verbose_name='date of publication')

    def __str__(self):
        return u'%s, %s' %(self.title, self.publisher)

    class Meta: 
        ordering = ['title']
