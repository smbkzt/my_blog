from django.db import models


class Contact(models.Model):
    email = models.EmailField(null=False)
    fullname = models.CharField(max_length=100, null=False)
    text = models.TextField(max_length=400, null=False)

    def __str__(self):
        return f'Feedback from {self.fullname}'
