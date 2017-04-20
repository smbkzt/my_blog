from django.db import models
from django.template.defaultfilters import slugify
from datetime import datetime


class BlogPost(models.Model):
    title = models.CharField(
        "Название статьи", max_length=100)
    preview = models.TextField("Превью")
    text = models.TextField("Текст")
    date = models.DateTimeField("Дата публикации", blank=True)
    slug = models.SlugField("Генерация ссылки", unique=True)
    # post_image = models.ImageField("Изображение")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        self.date = datetime.now()
        super(BlogPost, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "blogposts"

    def __str__(self):
        return f"ID: {self.id}. This post is about '{self.title}'"
