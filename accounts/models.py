from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Images(models.Model):


    name = models.CharField(blank=True,null=True,max_length=265)
    image_by = models.ForeignKey(User,related_name  ='pics',on_delete=models.CASCADE,null=True )
    image = models.ImageField(upload_to='media/UserImages',default=None,null=True,blank=True)
    uploaded_on = models.DateTimeField(default=timezone.now())


    def __str__(self):
        return self.name

class Files(models.Model):
    name = models.CharField(blank=True,null=True,max_length=256)

    posted_by= models.ForeignKey(User,related_name='docs',null=True ,on_delete=models.CASCADE)
    file = models.FileField(default=None,upload_to='media/UserFiles')
    uploaded_on = models.DateTimeField(default=timezone.now())


    def __str__(self):
        return self.name
