from django.views.generic import ListView
from django.shortcuts import get_object_or_404, render
from django.views import View


from .models import Guide
# Create your views here.

class GuideListView(ListView):
    template_name = 'guide/guide_list.html'
    queryset = Guide.objects.all()

class GuideDetailView(View):
    template_name = 'guide/guide_detail.html'
    def get(self, request, pk=None, *args, **kwargs):
        context = {}
        if pk is not None:
            obj = get_object_or_404(Guide, pk=pk)
            context['object'] = obj
        return render(request, self.template_name, context)

