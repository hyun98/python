from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class UserManager(BaseUserManager):
    def create_user(self, userID, birth, name, password, email, belong):
        if not userID:
            raise ValueError('Users must have an userID')

        user = self.model(
            email=self.normalize_email(email),
            belong=belong,
            userID=userID,
            name=name,
            birth=birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, userID, name, birth, email, belong, password):
        user = self.create_user(
            email=email,
            password=password,
            belong=belong,
            userID=userID,
            name=name,
            birth=birth,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True,
    )
    userID = models.CharField(
        max_length=255,
        unique=True,
    )
    belong = models.CharField(
        max_length=255,
    )
    birth = models.DateField()
    name = models.CharField(max_length=255, )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'userID'   # login 할 때 username에 쓰임
    REQUIRED_FIELDS = ['name', 'birth', 'email', 'belong']

    def __str__(self):
        return self.userID

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
