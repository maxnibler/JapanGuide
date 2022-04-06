from django.shortcuts import render
from django.views import View
# from django.core.management.utils import get_random_secret_key

class HomeView(View):
    def get(self, request):
        context = {}
        return render(request, 'pages/home_page.html', context)

class AccountView(View):
    def get(self, request):
        context = {}
        return render(request, 'pages/account_page.html', context)