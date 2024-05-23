from django.urls import path
from users.views import get_user_by_id, get_all_users, user_login, create_user

urlpatterns = [
    path('create', create_user),
    path('<uuid:id>', get_user_by_id),
    path('getall', get_all_users),
    path('login', user_login),
    
] 