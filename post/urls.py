from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.post_create_view, name='post-create'),
    path('<int:my_id>/', views.post_content_view, name='post-view'),
    path('<int:my_id>/delete/', views.post_delete_view, name='post-delete'),
    path('list/', views.post_list_view, name='post-list'),
]