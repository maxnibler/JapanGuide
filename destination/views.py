from django.urls import reverse
from django.shortcuts import get_object_or_404, render

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

class DestinationCreateView(CreateView):
    template_name = 'destination/destination_create.html'
    form_class = DestinationModelForm
    queryset = Destination.objects.all()

    def form_valid(self, form):
        return super().form_valid(form)


class DestinationDetailView(DetailView):
    template_name = 'destination/destination_detail.html'
    queryset = Destination.objects.all()


class DestinationListView(ListView):
    template_name = 'destination/destination_list.html'
    queryset = Destination.objects.all()


class DestinationUpdateView(UpdateView):
    template_name = 'destination/destination_create.html'
    form_class = DestinationModelForm
    queryset = Destination.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Destination, pk=id_)

    def form_valid(self, form):
        return super().form_valid(form)


class DestinationDeleteView(DeleteView):
    template_name = 'destination/destination_delete.html'

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Destination, pk=id_)

    def get_success_url(self):
        return reverse('destination-list')
