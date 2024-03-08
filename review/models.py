from django.db import models
from django.conf import settings # todo : add user
from author.models import Author

class Review(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    # user = ????
    text = models.TextField()