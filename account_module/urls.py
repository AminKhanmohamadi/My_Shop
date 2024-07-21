from django.urls import path
from .views import *
app_name = 'account_module'
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register_page'),
    path('login/', LoginView.as_view(), name='login_page'),
    path('logout/', LogoutView.as_view(), name='logout_page'),
    path('active-code/<email_active_code>/', ActiveView.as_view(), name='active_page'),
    path('reset-pass/<str:active_code>', ResetPassword.as_view() , name='reset_password'),
    path('forgot_pass/' , ForgetPasswordView.as_view() , name='forgot_pass_page'),
]