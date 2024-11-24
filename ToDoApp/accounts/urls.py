from django.urls import path
from . import views as account_views
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView

urlpatterns = [
    path('accounts/register/', account_views.register, name='register'),
    path('accounts/login/', account_views.user_login, name='login'),
    path('accounts/logout/', account_views.user_logout, name='logout'),
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('profile/', account_views.profile, name='profile'),
]
