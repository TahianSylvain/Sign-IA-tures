from django.db import models
from django.contrib.auth.models import User


class FilesAdmin(models.Model):
    owner = models.ForeignKey(
        User,blank=True,null=True,
        on_delete=models.CASCADE )
    adminupload = models.FileField(upload_to='', blank=True, null=True)
    
    def __str__(self):
        return self.adminupload.url
