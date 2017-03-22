from django.db import models
from django.utils import timezone

# Create your models here.
class Drive(models.Model):

    drive_name = models.CharField(
        max_length=255,
    )
    student_id = models.CharField(
        max_length=255,

    )
    drive_date = models.DateTimeField(default=timezone.now)
    def __str__(self):

        return ' '.join([
            self.drive_name,
            self.student_id,
			self.drive_date,
        ])