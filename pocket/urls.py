from django.conf.urls import url
from . import views

app_name = "pocket"
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'add-url', views.url_add, name="url_add"),
]
