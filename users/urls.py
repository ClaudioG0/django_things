from django.urls import path
from .views import login_view, signup_view, logout_view


app_name = 'users'

urlpatterns = [
    path('accounts/login/', login_view, name='login'),
    path('accounts/signup/', signup_view, name='signup'),
    path('accounts/logout/', logout_view, name='logout'),
]