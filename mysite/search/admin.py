from django.contrib import admin

# Register your models here.
from .models import CourseProvider, Course

# Register your models here.                                                                                                                           
admin.site.register(CourseProvider)
admin.site.register(Course)

