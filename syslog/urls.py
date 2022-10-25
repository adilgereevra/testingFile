from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name= 'home'),

    path('users/', include('users.urls')),
    path('authen/', include('authen.urls')), #token
    path('tables/', include('tables.urls')),
]
