from django.shortcuts import render

from .models import Post
# Create your views here.

def post_content_view(request):
    obj = Post.objects.get(id=1)
    context = {
        'title': obj.title,
        'content': obj.content
    }
    return render(request, "post/content.html", context)