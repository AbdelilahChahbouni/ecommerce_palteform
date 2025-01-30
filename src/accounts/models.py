from django.db import models
from django.contrib.auth.models import BaseUserManager


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
    
