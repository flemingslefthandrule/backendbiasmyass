from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class User(AbstractUser):

    displayname: str = models.CharField(max_length=30)
    username: str = models.CharField(max_length=30, unique=True)
    # email: str = models.EmailField(unique=True)
    bio: str = models.CharField(max_length=500)
    image: str | None = models.URLField(null=True, blank=True)
    password: str = models.CharField(max_length=100)

    def set_displayname(self) -> str:
        if self.displayname == "":
            self.displayname = self.username


class UserManager(BaseUserManager):
    def create_user(
        self, username: str, password: str
    ) -> User:

        user = User(username=username)
        user.set_password(password)
        user.save()

        return user

