from django.conf.urls import url
from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.index, name="articles"),
    url(r'^search/$', views.search, name="search"),
    url(r'^(?P<slug>[\w\-]+)/$', views.detail, name="detailed_view")
]
