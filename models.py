from django.db import models


class StudentContactDetails(models.Model):  
    stu_rollno =  models.CharField(max_length=12)  
    stu_firstname =  models.CharField(max_length=30)  
    stu_lastame =  models.CharField(max_length=30)  
    stu_streetAddress =  models.CharField(max_length=100)  
    stu_city =  models.CharField(max_length=20)  
    stu_district =  models.CharField(max_length=20)  
    stu_state =  models.CharField(max_length=20)  
    stu_pincode = models.IntegerField()  
    stu_homephone =  models.IntegerField()  
    stu_mobilephone =  models.IntegerField()  
    stu_emailid =  models.CharField(max_length=40)  


class StudentPersonal(models.Model):  
     MARITAL_STATUS= (  
        ('Single', 'Single'),  
        ('Married', 'Married'),  
     )  
     stu_rollno =  models.ForeignKey(StudentContactDetails)  
     stu_fathername =  models.CharField(max_length=30)    
     stu_mothername =  models.CharField(max_length=30)  
     stu_dob =  models.DateField()  
     stu_maritalstatus =  models.CharField(max_length=7, choices=MARITAL_STATUS)  
     stu_hobbies =  models.CharField(max_length=100)  
     stu_languagesknown =  models.CharField(max_length=100)    


class StudentSkills(models.Model):  
     stu_rollno =  models.ForeignKey(StudentContactDetails)   
     skill =  models.CharField(max_length=30)  


class StudentEduQualification(models.Model):  
     stu_rollno =  models.ForeignKey(StudentContactDetails)  
     course =  models.CharField(max_length=15)  
     institute =  models.CharField(max_length=30)  
     board =  models.CharField(max_length=30)  
     yearOfPass =  models.IntegerField()  
     marksObtained =   models.IntegerField()  


class StudentProjects(models.Model): 
     stu_rollno =  models.ForeignKey(StudentContactDetails)  
     projectName =  models.CharField(max_length=50)  
     technologiesUsed =  models.CharField(max_length=100)  
     projectDescription =  models.CharField(max_length=300)  


class StudentCertifications(models.Model):  
     CERTIFICATE_TYPE = (  
        ('Participated', 'Participated'),  
        ('Attended', 'Attended'),  
        ('Volunteered', 'Volunteered'),  
        ('Won', 'Won'),  
        ('Conducted', 'Conducted'),  
        ('Co-ordinated', 'Co-ordinated'),  
    )  
     stu_rollno =  models.ForeignKey(StudentContactDetails)  
     certificateType =  models.CharField(max_length=13, choices=CERTIFICATE_TYPE)  
     event =  models.CharField(max_length=30)  
     heldOn =  models.DateField()  
     heldAt =  models.CharField(max_length=30)  
     topic =   models.CharField(max_length=30)  


class StudentAwards(models.Model):  
     stu_rollno =  models.ForeignKey(StudentContactDetails)  
     wonAt =  models.CharField(max_length=30)  
     topic =  models.CharField(max_length=50)  
     wonOn =    models.DateField()  


class StudentActivities(models.Model):  
    stu_rollno =  models.ForeignKey(StudentContactDetails)  
    activity =  models.CharField(max_length=30)  