from django.urls import path

from . import views

urlpatterns = [
    path('', views.GuideListView.as_view(), name='guide-list'),
]
