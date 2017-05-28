from functools import reduce

from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import Http404
from django.db.models import Q

from .models import BlogPost


def welcome_page(request):
    """Renders welcome page"""

    return render(request, 'blog/welcome_page.html')


def about_page(request):
    """Renders about page"""

    return render(request, 'blog/about.html')


def articles(request):
    '''Returns index of blogposts'''

    if request.method == "GET":
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
    else:
        raise Http404()
    return render(request, 'blog/articles.html', context)


def search(request):
    """Article titles search method """

    if request.method == "GET":
        raise Http404()
    else:
        search_criterias = str(request.POST['search-articles']).strip()
        search_criterias = search_criterias.split(" ")
        all_posts = BlogPost.objects.filter(
            reduce(lambda x, y: x | y, [Q(title__contains=item) for item in search_criterias]))
        context = {
            "latest_posts": all_posts,
        }

    return render(request, 'blog/articles.html', context)


def detail(request, slug):
    """Renders detailed views of posts"""

    post = get_object_or_404(BlogPost, slug=slug)
    return render(request, 'blog/detail.html', {'post': post})
