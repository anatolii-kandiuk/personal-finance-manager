from django.urls import path

from .views import *


urlpatterns = [
    path('account/<int:pk>/', ViewUser.as_view(), name='view_account'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]

