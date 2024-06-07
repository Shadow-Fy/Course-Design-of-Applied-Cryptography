"""
URL configuration for 密码学课设 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from APP.views import login, register, addFriend, updateFriend, updateUserData, sendMsg, \
    get_image, msg_clean

urlpatterns = [
    path('api/login', login),
    path('api/addFriend', addFriend),
    path('api/updateFriend', updateFriend),
    path('api/register', register),
    path('api/updateUserData', updateUserData),
    path('api/sendMsg', sendMsg),
    path('api/get_image', get_image),
    path('api/msg_clean', msg_clean),
]
