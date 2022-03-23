from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField()
    created = models.DateTimeField(auto_now_add=True)
    likes_count = models.IntegerField(default=0)
    owner = models.ForeignKey(
        "auth.User", related_name="posts", on_delete=models.CASCADE
    )

    class Meta:
        ordering = ["created"]

    def likes(self):
        return self.likes

    def __str__(self):
        return self.title
