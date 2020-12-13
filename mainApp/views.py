from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Post


@login_required
def main_view(request):
    posts = Post.published.all()

    context = {
        'posts': posts
    }

    return render(request, 'mainApp/main.html', context)
