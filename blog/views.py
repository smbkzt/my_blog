from django.shortcuts import render, get_object_or_404
from .models import BlogPost


def welcome_page(request):
    return render(request, 'blog/welcome_page.html')


# def contact_page(request):
#     return render(request, 'blog/contact.html')


def about_page(request):
    return render(request, 'blog/about.html')


def index(request):
    '''Returns index of blogposts'''
    latest_posts = BlogPost.objects.order_by('-posted_date')[:5]
    context = {
        "latest_posts": latest_posts
    }
    return render(request, 'blog/index.html', context)


def detail(request, post_id):
    post = get_object_or_404(BlogPost, pk=post_id)
    context = {'post': post}
    return render(request, 'blog/detail.html', context)
