from django.db import models

class Realtor(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    is_mvp = models.BooleanField(dafault=False)
    hire_date = models.DateTimeField(default=datetime.now, blank=True)
    
    
    # Create your models here.
