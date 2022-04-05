from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home-page'),
    path('account/', views.account, name='account-page')
]