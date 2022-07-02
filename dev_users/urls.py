from django.urls import path
from .import  views

urlpatterns = [
    path('',views.profiles, name ="profiles"),
    path('profile/<str:pk>/',views.userProfile, name="user-profile"),
    path('login/',views.loginUser,name='login_user'),
    path('logout/',views.logoutUser,name='logout_user'),
]
