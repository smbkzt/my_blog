from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import BlogPost


def welcome_page(request):
    return render(request, 'blog/welcome_page.html')


# def contact_page(request):
#     return render(request, 'blog/contact.html')


def about_page(request):
    return render(request, 'blog/about.html')


def index(request):
    '''Returns index of blogposts'''
    all_posts = BlogPost.objects.order_by('-date')
    pagination = Paginator(all_posts, 3)
    page = request.GET.get('page')
    try:
        latest_posts = pagination.page(page)
    except PageNotAnInteger:
        latest_posts = pagination.page(1)
    except EmptyPage:
        latest_posts = pagination.page(pagination.num_pages)

    context = {
        "latest_posts": latest_posts,
    }
    return render(request, 'blog/index.html', context)


def detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    context = {'post': post}
    return render(request, 'blog/detail.html', context)
