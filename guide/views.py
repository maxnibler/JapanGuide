from django.views.generic import ListView
from django.shortcuts import render
from django.views import View


from .models import Guide
# Create your views here.

class GuideListView(ListView):
    template_name = 'guide/guide_list.html'
    queryset = Guide.objects.all()

