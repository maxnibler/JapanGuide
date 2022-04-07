from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home-page'),
    path('about/', views.AboutView.as_view(), name='account-page'),
    path('account/', views.AccountView.as_view(), name='account-page')
]