from django.db import models

class Requirements(models.Model):
    marksUG = models.CharField(max_length=150)
    experience = models.CharField(max_length=25)
    
    def __unicode__(self):
        return self.full_name

    def __unicode__(self):
        return self.street

class TechnicalSkills(models.Model):
    technology = models.CharField(max_length=200)
	

class Education(models.Model):
    School = models.CharField(max_length=100)
	Intermediate=models.CharField(max_length=100)
	Degree=models.CharField(max_length=100)
  
  def create(cls, email_address):
        key = hookset.generate_email_confirmation_token(email_address.email)
        return cls._default_manager.create(email_address=email_address, key=key)

      
