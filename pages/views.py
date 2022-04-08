from genericpath import exists
from django.shortcuts import render
from django.views import View

# from destination.models import Destination
from .models import PageText
# from django.core.management.utils import get_random_secret_key

class HomeView(View):
    def get(self, request):
        page_key = 'HO'
        queryset = PageText.objects.filter(page=page_key)
        context = {"objects": queryset}
        return render(request, 'pages/home_page.html', context)

class AboutView(View):
    template_name = 'pages/about_page.html'
    def get(self, request):
        page_key = 'AB'
        queryset = PageText.objects.filter(page=page_key)
        context = {"objects": queryset}
        return render(request, self.template_name, context)

class AccountView(View):
    def get(self, request):
        context = {}
        return render(request, 'pages/account_page.html', context)
