from django.db import models

# Create your models here.
class Student(models.Model):
    stu_reg_num = models.TextField(unique=True)
    stu_name = models.TextField()
    email = models.TextField()
    stu_mob = models.TextField(null=True)
    password = models.CharField(max_length=250)
    create_at = models.DateTimeField(auto_now=True)
    