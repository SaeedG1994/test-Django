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

    path('add-skill/',views.addSkill,name="add_skill"),
    path('update-skill/<str:pk>/',views.updateSkill,name="update_skill"),
    path('delete-skill/<str:pk>/',views.deleteSkill,name="delete_skill"),

    path('inbox',views.inbox,name='inbox'),
    path('viewmessage/<str:pk>/',views.viewMessage,name="view_message"),
    path('create-message/<str:pk>/',views.createMessage,name="create_message"),
]
