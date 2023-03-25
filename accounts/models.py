from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

# Create  Custom User Model
class MyAccountManger(BaseUserManager):
    # normal users validation
    def create_user(self,first_name,last_name,username,email,phone_number,password=None):
        if not email:
            raise ValueError('user must have an Email Address')
        if not username:
            raise ValueError('User must have username')
        if not phone_number:
            raise ValueError('User must have Mobile number')
        
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
        )

        user.set_password(password)
        user.save(using=self.db)
        return user
    
    #validating super users
    def create_superuser(self,first_name,last_name,username,email,password,phone_number):
        user=self.create_user(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password,
            phone_number=phone_number,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    username=models.CharField(max_length=50,unique=True)
    email=models.CharField(max_length=100,unique=True)
    phone_number=models.CharField(max_length=12,unique=True)

    # Required Field
    date_joined=models.DateTimeField(auto_now_add=True)
    last_login=models.DateTimeField(auto_now_add=True)
    is_admin=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=False)
    is_superadmin=models.BooleanField(default=False)


    USERNAME_FIELD ='email'
    REQUIRED_FIELDS=['username','first_name','last_name','phone_number']
    objects=MyAccountManger()

    def __str__(self):
        return self.email
    
    #Permission setup
    def has_perm(self,perm,obj=None):
        return self.is_admin
    
    def has_module_perms(self,add_label):
        return True

