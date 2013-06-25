#from django.conf import settings
#from django.db import models
 
 
 
#  
# class MyUser(AbstractBaseUser):
#     email = models.EmailField(unique=True)
#     USERNAME_FIELD = 'email'
#     first_name = models.CharField(blank=False) # might not work because overrides existing class
#     last_name = models.CharField(blank=False)  
#     REQUIRED_FIELDS = ['first_name', 'last_name']
#   
# class models.CustomUserManager):
#     def create_user(self, email, first_name, last_name, password): 
#         user =  self.model(email= email, first_name= first_name, last_name = last_name, is_active=True, is_superuser=False)
#         user.set_password(password)
#         user.save()
#         
#     def create_superuser(self, email, first_name, last_name, password): 
#         user =  self.model(email= email, first_name= first_name, last_name = last_name, is_active=True, is_superuser=True)
#         user.set_password(password)
#         user.save()
 # 
 # class UserProfile(models.Model):
 #     user = models.OneToOneField(settings.AUTH_USER_MODEL)
 #     activation_key = models.CharField(max_length=40)
 #     key_expires = models.DateTimeField()
 
 # WHEN CREATING DATABASE TABLES FOR CODE SNIPPETS def USE(self, 
    #  author = models.ForeignKey(settings.AUTH_USER_MODEL) 
    # cause it needs to link to the custom user model
    # 
 #    