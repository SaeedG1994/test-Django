from django.urls import path
from .import  views

urlpatterns = [
    path('',views.profiles, name ="profiles"),
    path('profile/<str:pk>/',views.userProfile, name="user-profile"),
    path('edit-profile/',views.editProfile,name="edit_profile"),
    path('account/',views.userAccount,name="user_account"),
    path('login/',views.loginUser,name="login_user"),
    path('logout/',views.logoutUser,name="logout_user"),
    path('register/',views.registerUser,name="register_user"),
]
