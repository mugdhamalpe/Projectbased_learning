from django.db import models
from django.contrib.auth.models import User, UserManager
 
class profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(default='default.jpg', upload_to='profile_pics')
    scan_image=models.ImageField(upload_to='scanning_pics')

    def __str__(self):
        return f'{self.user.username} Profile'



