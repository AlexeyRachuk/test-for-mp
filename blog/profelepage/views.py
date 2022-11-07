from django.shortcuts import render

from post.models import Post
from profelepage.models import UserPage


def profile_page(request):
    return render(request, 'author.html', {'profile_all': UserPage.objects.all().filter(user=request.user),
                                           'user_post_all': Post.objects.all().filter(user=request.user)})
