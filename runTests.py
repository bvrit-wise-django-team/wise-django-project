def multiply(a, b):
	return a * b;

def test_numbers_3_4():
    assert multiply(7, 5) == 35
    assert multiply(4, 7) == 28
class loginTest(TestCase):
    def setUp(self):
 self.client.login(username='14wh1a05b2', password='1234@5678')


from django.test import TestCase
from myapp.models import Student

class LoginTestCase(TestCase):
    def setUp(self):
        Student.objects.create(name="14wh1a05b2", password="123$5678")
        Student.objects.create(name="14wh1a0597", password="@123nandini")

    def test_login_in(self):
        stu5b2 = Student.objects.get(name="14wh1a05b2")
        stu597 = Student.objects.get(name="14wh1a0597")
        self.assertEqual(stu5b2.password(), 'password is "123$5678"')
        self.assertEqual(stu597.password(), ' password is"@123nandini"')
