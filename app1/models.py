from django.db import models

# Create your models here.
class jana(models.Model):
    name=models.CharField(max_length=10,verbose_name='ENTER NAME')
    age=models.IntegerField()
    email=models.EmailField()
    mobile=models.BigIntegerField(default=0,help_text='mobile no should be 10 digits')
    address=models.TextField(default='chennai')
    course=models.CharField(default='python',max_length=20,choices=[('python','PYTHON'),
                                                   ('java','JAVA'),
                                                   ('c','C'),
                                                   ('web design','WEB DESIGN')])
    datetime=models.DateTimeField(auto_now=True)
    image=models.ImageField(default='NULL')

class details(models.Model):
    name=models.CharField(max_length=10,verbose_name='ENTER NAME')
    age=models.IntegerField()
    email=models.EmailField(unique=True)
    mobile=models.BigIntegerField(help_text='mobile no should be 10 digits')
    address=models.TextField(default='chennai')
    course=models.CharField(default='python',max_length=20,choices=[('python','PYTHON'),
                                                   ('java','JAVA'),
                                                   ('c','C'),
                                                   ('web design','WEB DESIGN'),
                                                                    ('django','DJANGO'),
                                                                    ('c++','CPP'),
                                                                    ('advancejava','ADVANCE JAVA')])
    datetime=models.DateTimeField(auto_now=True)
    fees=models.BooleanField(default=False)