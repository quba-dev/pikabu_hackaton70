from django.db import models
from user.models import CustomUser
# from category.models import Category

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=500)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    url = models.URLField()
    poster = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f'{self.id}: {self.title} -> {self.poster}'


class Vote(models.Model):
    voter = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}: {self.voter} -> {self.post}'


class Comments(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='author_comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comments')
    text = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.author} {self.text}"
