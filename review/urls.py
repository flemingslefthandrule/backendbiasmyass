from django.urls import path, include

from review import views 

urlpatterns = [
    path('<str:slug>/reviews', views.ReviewView.as_view({'get': 'list', 'post': 'post'}),name="review")
]