from django.db import models
# from django.auth.models import USer

class FilesAdmin(models.Model):
    # owner = models.ForiegnKey(User, on_delete=models.CASCADE)
    adminupload = models.FileField(upload_to='media')
    
    def __str__(self):
        return self.adminupload.url