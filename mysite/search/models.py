from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import django.db.models.options as options

# Create your models here.

options.DEFAULT_NAMES = options.DEFAULT_NAMES + ('es_index_name', 'es_type_name', 'es_mapping')


class CourseProvider(models.Model):
    name = models.CharField(max_length=255, unique=True)
    address = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=1000, unique=True)
    contact_person = models.CharField(max_length=255, unique=True)
    url = models.URLField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    phone = models.CharField(max_length=255, unique=True)
    image = models.ImageField(max_length=255, unique=True)
    #courses = models.OneToManyField(Course, null=True, blank=True)


class Course(models.Model):
    name = models.CharField(max_length=500, blank=True) 
    instructor = models.CharField(max_length=500, blank=True)
    language = models.CharField(max_length=100, blank=True) 
    level = models.CharField(max_length=100, blank=True) 
    duration = models.IntegerField(blank=True)
    syllabus = models.CharField(max_length=1000, blank=True)
    cprovider = models.ForeignKey(CourseProvider, null=True, blank=True)

