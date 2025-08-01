from django.urls import path
from . import views

urlpatterns = [
    path('createtask/', views.TheTaskList.as_view()),
    path('updatetask/<int:pk>/', views.TheTask.as_view()),
    path('createuser/', views.UserList.as_view()),
    path('loginuser/', views.LoginUser.as_view()),
]
