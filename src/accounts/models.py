from django.db import models
from django.contrib.auth.models import BaseUserManager , AbstractBaseUser 
import pycountry

class MyAccountManager(BaseUserManager):
    def create_user(self , f_name , l_name , user_name , email , country , password):
        if not email :
            raise ValueError("User musst Have an email")
        elif not user_name:
            raise ValueError("User musst have A username")
        user = self.model(
            first_name = f_name,
            last_name = l_name,
            email = email,
            username = user_name,
            country = country,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_super_user(self , username , f_name , l_name , email , password):
        user = self.create_user(
            first_name = f_name,
            last_name = l_name,
            email= email,
            username = username,
        )
        
        user.is_active = True
        user.is_admin = True
        user.is_stuff = True
        user.is_superadmin = True 
        user.save(using= self._db)
        return user
    


class Account(AbstractBaseUser):
    @staticmethod
    def get_country():
        countries = list(pycountry.countries)
        country_choices = [(country.alpha_2 , country.name) for country in countries]
        return country_choices
    

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=100 , unique=True)
    username = models.CharField(max_length=100 , unique= True)
    phone_number = models.CharField(max_length=50)
    country = models.CharField(max_length=2 , choices=get_country() , default="US")

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)

    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)


    USERNAME_FIELD = "email"
    REQUIRED_FILEDS = ['last_name' , 'first_name']

    objects = MyAccountManager()

    def __str__(self):
        return self.username
    
    def has_perm(self , perm , obj=None):
        return self.is_admin
    
    def has_module_perms(self , app_label):
        return True
