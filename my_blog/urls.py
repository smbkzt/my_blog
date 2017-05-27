from django.conf.urls import url, include
from django.contrib import admin
from blog import views
from contact import views as contact_views

urlpatterns = [
    url(r'^$', views.welcome_page, name="welcome page"),
    url(r'^admin/', admin.site.urls),
    url(r'^contact/', contact_views.contact_page, name="contacts"),
    url(r'^about/', views.about_page, name="about"),
    url(r'^articles/', include('blog.urls')),
]
