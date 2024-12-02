from django.urls import path, include
from . import views as account_views
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView


urlpatterns = [
    path('accounts/register/', account_views.register, name='register'),
    path('accounts/login/', account_views.user_login, name='login'),
    path('accounts/logout/', account_views.user_logout, name='logout'),
    path('password_reset/', PasswordResetView.as_view(template_name='accounts/password_reset.html'), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_done'),
    path('profile/', account_views.profile, name='profile'),
    #path('account/dashboard/', account_views.dashboard, name='dashboard'),
    path('account/', include('dashboard.urls')),

]
