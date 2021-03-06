"""tradulive_back URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin

from rest_framework.schemas import get_schema_view

#schema_view = get_schema_view(title='Pastebin API')

#from openapi_codec import OpenAPICodec
#codec = OpenAPICodec()
#schema = codec.encode(schema_view)


from core.routers import urls as coreurls
from core.views import search, update_field

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(coreurls, namespace="api")),
 #   url(r'^schema/$', schema_view),
    url(r'^search/$', search),
    
    url(r'^update$', update_field),

]
