from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.post_create_view),
    path('<int:my_id>/', views.post_content_view),
    path('<int:my_id>/delete/', views.post_delete_view),
]