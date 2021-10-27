from django.db import models

class Post(models.Model):
    body = models.TextField()
    created = models.DateTimeField(auto_now=True, null=True)
    owner = models.ForeignKey(
        'users.User', related_name='posts', on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.body

class Comment(models.Model):
    body = models.TextField()
    created = models.DateTimeField(auto_now=True, null=True)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    owner = models.ForeignKey(
        'users.User', related_name='comments', on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.body
