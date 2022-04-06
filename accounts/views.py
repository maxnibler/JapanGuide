from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import authenticate
from django.urls import reverse_lazy
from django.views import generic, View

# Create your views here.

class SignupView(View):
    template_name = 'accounts/signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home-page')
        form = UserCreationForm()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        context = {'form': form}
        return render(request, self.template_name, context)


