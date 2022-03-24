from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler

from .models import Post


def reset_upvotes():
    """
    Resets upvotes
    """
    posts = Post.objects.all()
    for post in posts:
        post.likes_count = 0
        post.save()


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(reset_upvotes, "interval", minutes=1)
    scheduler.start()
