
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin,  BaseUserManager
from django.db import models


# 유저 매니저
class UserManger(BaseUserManager):
    def create_user(self, email, password, *args, **kwargs):
        if not email:
            raise ValueError('유저는 반드시 이메일 주소가 존재해야합니다.')
        user = self.create(email=email, *args, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, *args, **kwargs):
        user = self.create_user(email, password, *args, **kwargs)
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        return user


#유저
class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=100, verbose_name="유저")
    email = models.EmailField(unique=True,verbose_name="이메일")
    is_active = models.BooleanField(default=False,verbose_name="인증_유무")
    is_staff = models.BooleanField(default=False,verbose_name="관리자_유무")

    objects = UserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'

    def __str__(self):
        return self.name

    @property
    def username(self):
        return self.name


