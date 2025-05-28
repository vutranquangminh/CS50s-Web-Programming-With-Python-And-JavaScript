from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Post(models.Model):
    content = models.CharField(max_length=140)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Post {self.id} by {self.author.username} on {self.timestamp.strftime('%d %b %Y %H:%M:%S')}"

    class Meta:
        ordering = ['-timestamp']


class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')

    def __str__(self):
        return f"{self.follower.username} is following {self.following.username}"

    class Meta:
        unique_together = ('follower', 'following')
        verbose_name = 'Follow'
        verbose_name_plural = 'Follows'


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')

    def __str__(self):
        return f"{self.user.username} liked post {self.post.id} with content '{self.post.content}' by {self.post.author.username}"

    class Meta:
        unique_together = ('user', 'post')
        verbose_name = 'Like'
        verbose_name_plural = 'Likes'
