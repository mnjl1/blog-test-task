from django.urls import path
from api import views


urlpatterns = [
    path("posts/", views.get_posts),
    path("posts/<int:pk>/", views.get_post_by_id),
    path("create/post/", views.create_post),
    path("posts/<int:pk>/update", views.update_post),
    path("posts/<int:pk>/delete", views.delete_post),
    path("posts/<int:pk>/upvote", views.upvote_post),
]
