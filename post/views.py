from django.shortcuts import render

from .forms import PostForm
from .models import Post
# Create your views here.

def post_create_view(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }
    return render(request, "post/create.html", context)

def post_content_view(request):
    obj = Post.objects.get(id=1)
    context = {
        'title': obj.title,
        'content': obj.content
    }
    return render(request, "post/content.html", context)