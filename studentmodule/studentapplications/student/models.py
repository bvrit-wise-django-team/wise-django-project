from django.db import models
class StudentContactDetails(models.Model):
    stu_rollno = models.CharField(max_length=12)
    stu_firstname = models.CharField(max_length=30)
 