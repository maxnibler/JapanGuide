from django.shortcuts import render, get_object_or_404, redirect

from .forms import PostForm, RawPostForm
from .models import Post
# Create your views here.

def post_create_view(request):
    form = RawPostForm()
    if request.method == "POST":
        form = RawPostForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            Post.objects.create(**form.cleaned_data)
        else:
            print(form.errors)
    context = {
        'form': form,
    }
    return render(request, "post/create.html", context)

# def post_create_view(request):
#     form = PostForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#     context = {
#         'form': form
#     }
#     return render(request, "post/create.html", context)

# def post_content_view(request):
#     obj = Post.objects.get(id=1)
#     context = {
#         'title': obj.title,
#         'content': obj.content
#     }
#     return render(request, "post/content.html", context)

def post_content_view(request, my_id):
    obj = get_object_or_404(Post, id=my_id)
    context = {
        'title': obj.title,
        'content': obj.content
    }
    return render(request, "post/content.html", context)

def post_delete_view(request, my_id):
    obj = get_object_or_404(Post, id=my_id)

    if request.method == "POST":
        obj.delete()
        return redirect('../')

    context = {
        'title': obj.title,
    }
    return render(request, "post/delete.html", context)

def post_list_view(request):
    queryset = Post.objects.all()
    context = {
        'object_list': queryset,
    }
    return render(request, "post/list.html", context)

