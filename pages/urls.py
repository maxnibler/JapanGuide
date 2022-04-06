from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home-page'),
    path('account/', views.AccountView.as_view(), name='account-page')
]