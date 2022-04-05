from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.post_create_view),
    path('', views.post_content_view),
]