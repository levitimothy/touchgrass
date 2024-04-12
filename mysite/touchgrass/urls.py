from . import views
from django.urls import path

app_name = 'tg'
urlpatterns = [
    path('', views.home, name='home'),
    path('newpost/', views.newpost, name='newpost'),
]
