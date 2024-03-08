from django.db import models
from django.utils.text import slugify
from django.urls import reverse

class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.CharField(max_length=500)
    work = models.CharField(max_length=100)
    summary = models.CharField(max_length=500)
    photo = models.CharField(max_length=100)
    slug = models.SlugField(unique=True,max_length=100)
    url = models.CharField(max_length=500)

    def url_make(self)->str:
        return reverse(
            "what_author",
            kwargs={
                "author_id": self.id,
                "slug": self.slug
            }
        )

    def __str__(self):
        return self.name