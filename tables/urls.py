from django.urls import path, include
from tables import views 


urlpatterns = [
    path('tables/', views.create, name='create smt'),

]