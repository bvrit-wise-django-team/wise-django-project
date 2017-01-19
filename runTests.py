from django.test import TestCase
from models import StudentSkills

class StudentSkillsTestCase(TestCase):
    def setUp(self):
        StudentSkills.objects.create(stu_rollno="1", skill="java")
        StudentSkills.objects.create(stu_rollno="2", skill="django")

   
