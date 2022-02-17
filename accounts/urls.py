from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.index, name='home'),
    path('login/', views.LogIn, name='LogIn')
]
