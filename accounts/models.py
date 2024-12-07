import uuid
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.db import models
from .userManager import UserManager
class User(AbstractBaseUser, PermissionsMixin):
   ROLES = (
        ('admin', 'Admin'),
        ('user', 'User'),
    )
   public_id = models.UUIDField(db_index=True, unique=True, default=uuid.uuid4, editable=False)
   role = models.CharField(max_length=10, choices=ROLES, default='user')
   username = models.CharField(db_index=True,max_length=255, unique=True)
   first_name = models.CharField(max_length=255)
   last_name = models.CharField(max_length=255)
   email=models.EmailField(db_index=True,unique=True,)

   is_active=models.BooleanField(default=True)
   is_staff=models.BooleanField(default=False)
   created=models.DateTimeField(auto_now_add=True)
   updated=models.DateTimeField(auto_now=True)
   USERNAME_FIELD = 'email'
   REQUIRED_FIELDS = ['username']
   objects=UserManager()
   def __str__(self):
       return f"{self.username}"
   @property
   def name(self):
       return f"{self.first_name} {self.last_name}"