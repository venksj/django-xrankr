from django.core.management.base import BaseCommand
from search.models import CourseProvider, Course
from model_mommy import mommy

import random
import names

class Command(BaseCommand):
    help = "Management command to push data to DB"

    def add_arguments(self, parser):
        parser.add_argument('count', nargs=1, type=int)

    def handle(self, *args, **options):
        print ("This is a surprise!!")

        self.clear()
        self.make_course_providers()
        self.make_courses(options)


    def make_course_providers(self):
        cp_instances = (
                {"name": 'PIKDUP', "url": "www.pikdup.com", "email": "contact@pikdup.com"}, 
                {"name": 'UPX', "url": "www.upx.com", "email": "contact@upx.com"}, 
                {"name": 'UNACADEMY', "url": "www.unacademy.com", "email": "contact@unacademy.com"}, 
                {"name": 'BYJU', "url": "www.byju.com", "email": "contact@byju.com"}, 
                {"name": 'SIMPLILEARN', "url": "www.simplilearn.com", "email": "contact@simplilearn.com"}, 
                {"name": 'VEDANTU', "url": "www.vedantu.com", "email": "contact@vedantu.com"}
                )

        self.course_providers = []
        for inst in cp_instances:
            cp = mommy.make(
                CourseProvider,
                name = inst["name"],
                url = inst["url"],
                email = inst["email"],
                contact_person = names.get_full_name(),
            )
            self.course_providers.append(cp)


    def make_courses(self, options):
        crs_names = ( "Intro to Big data", 
                "Intro to Python", 
                "HTML and CSS" , 
                "Web development", 
                "Full-stack developer program", 
                "Machine Learning", 
                "Deep Learning and Neural networks", 
                "Self driving car", 
                "Artificial Intelligence", 
                "Hurricanes", 
                "Stock Market fundamentals", 
                "Options and Futures", 
                "Day Trading Fundamentals", 
                "Digital Marketing", 
                "Social Media"
                )

        crs_level = ("Beginner",
                "Intermediate",
                "Advanced",
                "Degree"
                )

        self.courses = []
        for _ in range(options.get('count')[0]):
            crs = mommy.prepare(
                Course,
                name = random.choice(crs_names),
                instructor = names.get_full_name(),
                language = "English",
                level = random.choice(crs_level),
                cprovider=random.choice(self.course_providers),
            )
            self.courses.append(crs)
        Course.objects.bulk_create(self.courses)


    def clear(self):
        CourseProvider.objects.all().delete()
        Course.objects.all().delete()


