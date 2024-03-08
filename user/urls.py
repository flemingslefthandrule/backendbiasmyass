from django.urls import path, include
from rest_framework.routers import DefaultRouter # eno

from user import views 

profile_router = DefaultRouter(trailing_slash=False)
profile_router.register('profiles', views.ProfileView)

urlpatterns = [
    path('login', views.login, name="login"),
    path('signup', views.signup, name="signup"),
    path('user', views.UserView.as_view(), name="profile"),
     path('', include(profile_router.urls))
]