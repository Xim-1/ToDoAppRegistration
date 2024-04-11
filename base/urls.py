from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView
from . import views as v

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', v.logout_view, name='logout_view'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('create-task/', TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name='task-delete'),

]