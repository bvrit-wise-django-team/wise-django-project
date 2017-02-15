def add(a, b):
	return a + b;

def test_numbers_3_4():
    assert multiply(3, 5) == 8
    assert multiply(4, 7) == 11

from django.test import TestCase
from models import StudentSkills

class StudentSkillsTestCase(TestCase):
    def setUp(self):
        StudentSkills.objects.create(stu_rollno="1", skill="java")
        StudentSkills.objects.create(stu_rollno="2", skill="django")

        def test_login_in(self):
        	student1 = Student.objects.get(stu_rollno="1")
        	student2 = Student.objects.get(stu_rollno="2")
        	self.assertEqual(student1.skill(), 'skill is java"')
        	self.assertEqual(student2.skill(), 'skill is django"')
