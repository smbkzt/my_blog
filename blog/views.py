from django.http import HttpResponse


def index(request):
    '''Returns index of blogposts'''
    return HttpResponse("Hello, this is index page of blog archives")
