from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignupView.as_view(), name='signup-page'),
    path('signin/', views.SigninView.as_view(), name='signin-page'),
]
