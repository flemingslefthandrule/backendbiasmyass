from django.db import models
from django.utils.text import slugify
from django.urls import reverse

class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.CharField(max_length=500)
    photo = models.CharField(max_length=100)
    url = models.SlugField(unique=True,max_length=100)

    def url_make(self)->self:
        return reverse(
            "what_author",
            kwargs={
                "author_id" = self.id,
                "url" = self.url
            }
        )

    def __str__(self):
        return self.name