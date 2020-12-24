from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    article_url = models.URLField(unique=True, max_length=255)
    created_at = models.DateTimeField()
    posted_by = models.CharField(max_length=255, blank=True, null=True)
    author = models.CharField(max_length=255, blank=True, null=True)
    translator = models.CharField(max_length=255, blank=True, null=True)
    editor = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f'{self.created_at}-{self.title}'
