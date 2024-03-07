from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(
        self, username: str, password: str
    ) -> User:

    user = User(username=username)
    user.set_password(password)
    user.save()

    return user

class User(AbstractUser):

    displayname: str = models.CharField(max_length=30)
    username: str = models.CharField(max_length=30, unique=True)
    # email: str = models.EmailField(unique=True)
    image: str | None = models.UrlField(null=True, blank=True)
    password: str = models.CharField(max_length=100)

    def set_displayname(self) -> self:
        if !(self.displayname):
            self.displayname = self.username