from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import django.db.models.options as options

# Create your models here.

options.DEFAULT_NAMES = options.DEFAULT_NAMES + ('es_index_name', 'es_type_name', 'es_mapping')


class CourseProvider(models.Model):
    name = models.CharField(max_length=255, unique=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True)
    contact_person = models.CharField(max_length=255, blank=True, null=True)
    url = models.URLField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(max_length=255, blank=True, null=True)
    #courses = models.OneToManyField(Course, null=True, blank=True)
    
    def __str__(self):  
        return ("Name(%s) URL(%s) Email(%s) Phone(%s)") %(self.name, self.url, self.email, self.phone)


class Course(models.Model):
    name = models.CharField(max_length=500, blank=False, null=False) 
    instructor = models.CharField(max_length=500, blank=True, null=True)
    language = models.CharField(max_length=100, blank=True, null=True) 
    level = models.CharField(max_length=100, blank=True, null=True) 
    duration = models.CharField(max_length=100, blank=True, null=True)
    syllabus = models.CharField(max_length=1000, blank=True, null=True)
    cprovider = models.ForeignKey(CourseProvider, null=True, blank=True)

    class Meta:
        es_index_name = 'vjdjango'
        es_type_name = 'course'
        es_mapping = {
            'properties': {
                'cprovider': {
                    'type': 'object',
                    'properties': {
                        'name': {'type': 'string', 'index': 'not_analyzed'},
                        'url': {'type': 'string', 'index': 'not_analyzed'},
                        'email': {'type': 'string', 'index': 'not_analyzed'},
                        'address': {'type': 'string', 'index': 'not_analyzed'},
                    }
                },

                'name': {'type': 'string', 'index': 'not_analyzed'},
                'instructor': {'type': 'string', 'index': 'not_analyzed'},
                'language': {'type': 'string'},
                'level': {'type': 'string'},
                'duration': {'type': 'string'},
                'syllabus': {'type': 'string'},

                'name_autocomplete': {
                    'type': 'completion',
                    'analyzer': 'simple',
                    'payloads': True,
                    'preserve_separators': True,
                    'preserve_position_increments': True,
                    'max_input_length': 100,
                },
            }
        }


    def __str__(self):  
        return ("Name(%s) Instructor(%s) Level(%s) Cprovider(%s)") %(self.name, self.instructor, self.level, self.cprovider)

    def es_repr(self):
        data = {}
        mapping = self._meta.es_mapping
        data['_id'] = self.pk

        for field_name in mapping['properties'].keys():
            data[field_name] = self.field_es_repr(field_name)

        return data


    def field_es_repr(self, field_name):
        config = self._meta.es_mapping['properties'][field_name]

        if hasattr(self, 'get_es_%s' % field_name):
            field_es_value = getattr(self, 'get_es_%s' % field_name)()
        else:
            if config['type'] == 'object':
                related_object = getattr(self, field_name)
                field_es_value = {}
                field_es_value['_id'] = related_object.pk

                for prop in config['properties'].keys():
                    field_es_value[prop] = getattr(related_object, prop)
            else:
                field_es_value = getattr(self, field_name)

        return field_es_value


    def get_es_name_autocomplete(self):
        return {
            "input": [self.name],
            "output": "%s" % (self.name),
            "payload": {"pk": self.pk},
        }


