from django.conf.urls import url, include
from django.contrib import admin
from blog import views

urlpatterns = [
    url(r'^$', views.welcome_page, name="welcome page"),
    url(r'^admin/', admin.site.urls),
    url(r'^contact/', views.contact_page, name="contacts"),
    url(r'^about/', views.about_page, name="about"),
    url(r'^blog/', include('blog.urls')),
]
