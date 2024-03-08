from django.urls import path, include 
from rest_framework.routers import DefaultRouter

from author import views 

author_router = DefaultRouter(trailing_slash=False)
author_router.register('', views.AuthorView)

urlpatterns = [
    path('', include(author_router.urls))
]