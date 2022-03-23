from django.urls import path
from api import views


urlpatterns = [
    path('api/posts/', views.get_posts),
    path('api/posts/<int:pk>/', views.get_post_by_id),
    path('api/create/post/', views.create_post),
]