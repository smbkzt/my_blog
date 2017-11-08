from django.db import models
from django.contrib.auth.models import User


class Pocket(models.Model):
    title = models.CharField("Article title", max_length=100)
    url = models.CharField("Article url", max_length=200)
    paragraph = models.TextField("Article body")
    user = models.ForeignKey(User)

    def __str__(self):
        return self.title
