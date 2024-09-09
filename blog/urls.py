# File blog/urls.py wasn't originally created, so we added it

from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
#    path('3', views.detail, name='detail'),
    path('<int:blog_id>/', views.detail, name='detail'),
]

