import uuid
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):

    @classmethod
    def _validate(cls, **kwargs) -> None:
        for k, v in kwargs.items():
            if not k:
                raise ValueError('You have not entered %s' % v)

    def _create(self, email: str, username: str, password: str, **extra) -> None:
        self._validate(email=email, username=username, password=password)
        user = self.model(email=self.normalize_email(email), username=username,
                          **extra)
        user.set_password(raw_password=password)
        user.save()

    def create_user(self,
                    email: str,
                    username: str,
                    password: str) -> None:
        self._create(email, username, password, )

    def create_superuser(self,
                         email: str,
                         username: str,
                         password: str) -> None:
        self._create(email, username, password, is_staff=True, is_superuser=True, is_active=True)


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    username = models.CharField(max_length=225, null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True, verbose_name='personal_email')

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username', ]


    objects = UserManager()

    def __str__(self):
        return f'{self.id} -- {self.email}'


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='static/img')

    def __str__(self):
        return self.user
