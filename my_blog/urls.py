from django.conf.urls import url, include
from django.contrib import admin
from blog import views
from contact import views as contact_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', views.welcome_page, name="welcome page"),
    url(r'^articles/', include('blog.urls')),
    url(r'^contact/', contact_views.contact_page, name="contacts"),
    url(r'^about/', views.about_page, name="about"),

    url(r'^pocket/', include('pocket.urls')),

    url(r'^draceditor/', include('draceditor.urls')),
]
