#sampleTests
def multiply(a , b):
	return a * b;

def test_numbers_3_4():
    assert multiply(4, 5) == 20
    assert multiply(4, 7) == 28
	
from django.test import TestCase
from myapp.models import Student

class StudentTestCase(TestCase):
    def setUp(self):
        Student.objects.create(name="xyz") 
	Student.objects.create(qualification="b.tech")
def test_student_details(self):
        name1 = Student.objects.get(name="xyz")
        quali1 = Student.objects.get(name="b.tech")
	self.assertEqual(name1.name(), 'xyz"')
        self.assertEqual(quali.qualification(), 'b.tech"')

