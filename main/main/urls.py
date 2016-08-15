"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from blogs.views import *
from django.conf import settings
from django.conf.urls import include

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blogs/$', blogHome,name='blogHome'),
    url(r'^blogs/(?P<blogauthor>[0-9A-Za-z_\-]+)/$', authorHome,name='authorHome'),
    url(r'^blogs/(?P<blogauthor>[0-9A-Za-z_\-]+)/(?P<category>[0-9A-Za-z_\-]+)/$', category,name='category'),
    url(r'^blogs/(?P<blogauthor>[0-9A-Za-z_\-]+)/(?P<category>[0-9A-Za-z_\-]+)/(?P<blogname>[0-9A-Za-z_\-]+)/$', blogView,name='blogview'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)