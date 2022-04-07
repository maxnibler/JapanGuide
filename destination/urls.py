from django.urls import path

from . import views

urlpatterns = [
    path('', views.DestinationListView.as_view(), name='destination-list'),
    path('<int:pk>/', views.DestinationDetailView.as_view(), name='destination-detail'),
    path('create/', views.DestinationCreateView.as_view(), name='destination-create'),
    path('<int:pk>/update/', views.DestinationUpdateView.as_view(), name='destination-update'),
    path('<int:pk>/delete/', views.DestinationDeleteView.as_view(), name='destination-delete'),
]