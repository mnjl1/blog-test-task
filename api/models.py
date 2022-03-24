from django.db import models


class Post(models.Model):
    """
    Post
    """

    title = models.CharField(max_length=255)
    link = models.URLField()
    created = models.DateTimeField(auto_now_add=True)
    likes_count = models.IntegerField(default=0)
    owner = models.ForeignKey(
        "auth.User", related_name="posts", on_delete=models.CASCADE
    )

    class Meta:
        ordering = ["created"]

    def __str__(self):
        return f"{self.title}, likes: {self.likes_count}"


class Comment(models.Model):
    """
    Comment
    """

    author = models.ForeignKey(
        "auth.User", related_name="users", on_delete=models.CASCADE
    )
    content = models.TextField(blank=False)
    created = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)

    class Meta:
        ordering = ["created"]
