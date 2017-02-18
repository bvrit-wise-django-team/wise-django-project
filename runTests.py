def multiply(a, b):
	return a * b;

def test_numbers_3_4():
    assert multiply(4, 5) == 20
    assert multiply(4, 7) == 28
	
from django.test import TestCase
from remarks.models import Remarks
from django.utils import timezone
#from django.core.urlresolvers import reverse


# models test
class RemarksTest(TestCase):

    def create_remarks(self, title="only a test", body="yes, this is only a test"):
        return Remarks.objects.create(title=title, body=body, created_at=timezone.now())

    def test_remarks_creation(self):
        w = self.create_remarks()
        self.assertTrue(isinstance(w, Remarks))
        self.assertEqual(w.__unicode__(), w.title)
	

