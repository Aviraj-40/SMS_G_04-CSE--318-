from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=50)
    dept = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
