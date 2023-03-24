from django.db import models

# Create your models here.
class Courses(models.Model):
    course_name = models.CharField(max_length=300, primary_key = True)
    faculty= models.CharField(max_length=100)
    points_requirements=models.IntegerField()
    subject_requirements=models.CharField(max_length=300)
    course_description=models.TextField()
    careers_offered=models.TextField()
    
   

class degree(models.Model):
    course_name = models.CharField(max_length=300,primary_key = True)
    faculty= models.CharField(max_length=100)
    points_requirements=models.IntegerField()
    subject_requirements=models.CharField(max_length=300)
    course_description=models.TextField()
    careers_offered=models.TextField()
    

    

def __str__(self):
    return self.course_name



    

