from django.db import models

# Create your models here.
class AdminBase(models.Model):
    name = models.CharField(blank=True, max_length=20)
    email = models.CharField(blank=True, max_length=20)
    phone = models.CharField(blank=True, max_length=20)
    logo = models.ImageField(blank=True, upload_to='logo/')
    street = models.CharField(blank=True, max_length=20)
    
    baner01 = models.ImageField(blank=True, upload_to='baner/')
    baner02 = models.ImageField(blank=True, upload_to='baner/')
    baner03 = models.ImageField(blank=True, upload_to='baner/')
    
    cookies = models.BooleanField(default=True)
    cookies_text = models.TextField(blank=True)
    
    commission = models.IntegerField(default=5)
    mode_demo = models.BooleanField(default=False)
    
    def __strt__(self):
        return self.name