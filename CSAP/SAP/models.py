from django.db import models

# Create your models here.
class Student(models.Model):
    studentname=models.CharField(max_length=40)
    coursename=models.CharField(max_length=40)
    courseid=models.CharField(max_length=10,default='Nill')
    semester = models.IntegerField(default=0)
    semester_mark=models.IntegerField(default=0)
    semester_attendance=models.IntegerField(default=0)
    status=models.CharField(max_length=5,default='None')

    def __str__(self):
        return self.studentname