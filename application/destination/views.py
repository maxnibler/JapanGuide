from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView,
)


from .models import Destination
from .forms import DestinationModelForm
# Create your views here.

class DestinationCreateView(View):
    template_name = 'destination/destination_create.html'
    queryset = Destination.objects.all()
    def get(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect('home-page')
        context = {'form': DestinationModelForm}
        return render (request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect('home-page')
        form = DestinationModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('destination-list')
        context = {'form': self.form_class}
        return render (request, self.template_name, context)
        

class DestinationDetailView(View):
    template_name = 'destination/destination_detail.html'
    def get(self, request, pk=None, *args, **kwargs):
        context = {}
        if pk is not None:
            obj = get_object_or_404(Destination, pk=pk)
            context['object'] = obj
        return render(request, self.template_name, context)


class DestinationListView(ListView):
    template_name = 'destination/destination_list.html'
    queryset = Destination.objects.all()


class DestinationUpdateView(UpdateView):
    template_name = 'destination/destination_create.html'
    def get_object(self):
        pk = self.kwargs.get('pk')
        obj = None
        if pk is not None:
            obj = get_object_or_404(Destination, pk=pk)
        return obj

    def get(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect('home-page')
        obj = self.get_object()
        context = {
            'object': obj,
            'form': DestinationModelForm(instance=obj),
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect('home-page')
        obj = self.get_object()
        form = DestinationModelForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
        context = {'form': form, 'object': obj}
        return render (request, self.template_name, context)

# class DestinationUpdateView(UpdateView):
#     template_name = 'destination/destination_create.html'
#     form_class = DestinationModelForm
#     queryset = Destination.objects.all()

#     def get_object(self):
#         id_ = self.kwargs.get("pk")
#         return get_object_or_404(Destination, pk=id_)

#     def form_valid(self, form):
#         return super().form_valid(form)


class DestinationDeleteView(View):
    template_name = 'destination/destination_delete.html'
    def get(self, request, pk=None, *args, **kwargs):
        if not request.user.is_staff:
            return redirect('home-page')
        context = {}
        if pk is not None:
            obj = get_object_or_404(Destination, pk=pk)
            context['object'] = obj
        return render(request, self.template_name, context)
    
    def post(self, request, pk=None, *args, **kwargs):
        if not request.user.is_staff:
            return redirect('home-page')
        if pk is not None:
            obj = get_object_or_404(Destination, pk=pk)
            obj.delete()
            return redirect('../../')
        return render(request, self.template_name, {})
