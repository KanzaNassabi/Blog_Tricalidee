from django.db import models
from rolepermissions.roles import assign_role, clear_roles
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default ='default.jpg', upload_to='profile_pics/',null=True)
    type = models.CharField(max_length=20,default ='Anonymous',null=True,choices=(
            ("Admin", "Admin"),
            ("Author", "Author"),
            ("Reader", "Reader"),
        ))
    new_type = models.CharField(max_length=20,default ='Anonymous',null=True)
    change_role = models.BooleanField(default=False)
    approved_user = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
    
    def approve(self):
        self.approved_user = True
        self.save()

    def set_change_role(self):
        self.change_role = True
        self.save()

    def changeRole(self):
        clear_roles(self.user)
        if self.new_type =="Admin":
            assign_role(self.user,'admin')     
        elif self.new_type =="Author":
            assign_role(self.user,'author')
        else:
            assign_role(self.user,'registreduser')
        self.type = self.new_type
        self.change_role = False
        self.new_type = 'Anonymous'
        self.save()
 

 