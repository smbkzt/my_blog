from django.db import models


class BlogPost(models.Model):
    post_article = models.CharField(
        "Название статьи", max_length=100, null=False)
    post_body = models.TextField("Текст", null=False)
    posted_date = models.DateTimeField("Дата публикации", null=True)
    # post_image = models.ImageField("Изображение")

    class Meta:
        verbose_name_plural = "blogposts"

    def __str__(self):
        return f"ID: {self.id}. This post is about '{self.post_article}'"