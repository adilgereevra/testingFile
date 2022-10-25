from django.urls import path, include
# from django.views.generic import TemplateView
# from django.conf import settings



# urlpatterns = [    
#     path('auth/', include('djoser.urls')), #token
#     path('auth/', include('djoser.urls.authtoken')), #token
#     path('auth/', include('djoser.urls.jwt')),
# ]

from rest_framework.authtoken import views


urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token)
]