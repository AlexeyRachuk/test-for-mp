from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from post.models import Post


def redirect_view(request):
    response = redirect('/blog')
    return response


class PostView(ListView):
    model = Post
    queryset = Post.objects.filter(draft=True).order_by('postdate')
    template_name = 'index.html'
    paginate_by = 12


class PostDetailView(DetailView):
    model = Post
    slug_field = 'url'
    template_name = 'post.html'
    context_object_name = 'post'
