import os

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Contest_author')
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, blank=True, related_name='Contest_voter')  # voter 추가
    upload_files = models.FileField(null=True, blank=True, verbose_name='파일')
    filename = models.CharField(max_length=64, null=True, verbose_name='첨부파일명')

    def delete(self, *args, **kargs):
        if self.upload_files:
            os.remove(os.path.join(settings.MEDIA_ROOT, self.upload_files.path))
        super(Post, self).delete(*args, **kargs)

    def __str__(self):
        return self.subject


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Contest_comment_author')
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    question = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE)
