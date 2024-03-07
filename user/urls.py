from django.urls import path, include

from user import views 

urlpatterns = [
    path('login', views.login, name="login"),
    path('signup', views.signup, name="signup"),
    path('user', views.UserView.as_view(), name="profile")
]