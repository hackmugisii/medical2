from django.urls import path
from .views import *

urlpatterns = [
    path('', chat_view, name='chatroom'),
    path('auth/', login_view, name='login'),
    path('auth/', register_view, name='register'),
    path('profile/', profile, name='profile'),
]
