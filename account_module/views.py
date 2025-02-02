from django.shortcuts import render ,redirect
from django.urls import reverse
from .models import User
from django.views import View
from django.utils.crypto import get_random_string
from account_module.forms import RegisterForm , LoginForm ,ForgotForm , ResetPasswordForm
from django.http import Http404
from django.contrib.auth import login , logout
from utils.email_service import send_email

# Create your views here.


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        context = {'register_form': register_form}
        return render(request ,'account_module/register.html' , context)

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_email = register_form.cleaned_data['email']
            user_password = register_form.cleaned_data['password']
            user:bool = User.objects.filter(email__iexact=user_email).exists()
            if user:
                register_form.add_error('email', 'ایمیل وارد شده تکراری میباشد')
            else:
                new_user = User(email=user_email , email_active_code=get_random_string(72) , is_active=False , username=user_email)
                new_user.set_password(user_password)
                new_user.save()
                send_email('فعال سازی حساب کاربری' , new_user.email , {'user':new_user} , 'emails/activate_user.html')
                return redirect(reverse('account_module:login_page'))


        context = {'register_form': register_form}
        return render(request, 'account_module/register.html', context)



class LoginView(View):
    def get(self, request):
        login_form = LoginForm()
        context = {'login_form': login_form}
        return render(request , 'account_module/login_module.html' , context)

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_email = login_form.cleaned_data.get('email')
            user_password = login_form.cleaned_data.get('password')
            user = User.objects.filter(email__iexact=user_email).first()
            if user is not None:
                if not user.is_active:
                    login_form.add_error('email' , 'حساب کاربری شما فعال نشده است')
                else:
                    is_password_correct = user.check_password(user_password)
                    if is_password_correct:
                        login(request, user)
                        return redirect(reverse('home_module:home'))
                    else:
                        login_form.add_error('email' , 'نام کاربری یا کلمه عبور اشتباه است')
            else:
                login_form.add_error('email' , 'کاربری با مشخصات وارد شده یافت نشد')

        context = {'login_form': login_form}
        return render(request, 'account_module/login_module.html', context)




class ActiveView(View):
    def get(self, request , email_active_code):
        user = User.objects.filter(email_active_code__iexact=email_active_code).first()
        if user is not None:
            if not user.is_active:
                user.is_active = True
                user.email_active_code = get_random_string(72)
                user.save()
                # todo: show message
                return redirect(reverse('account_module:login_page'))
            else:
                # todo : show your account was activated message to user
                pass
        raise Http404


class ForgetPasswordView(View):
    def get(self, request):
        forgot_pass_form = ForgotForm()
        context = {'forgot_pass_form': forgot_pass_form}
        return render(request , 'account_module/forget_pass.html' , context)

    def post(self, request):
        forgot_pass_form = ForgotForm(request.POST)
        if forgot_pass_form.is_valid():
            user_email = forgot_pass_form.cleaned_data.get('email')
            user = User.objects.filter(email__iexact=user_email).first()
            if user is not None:
                send_email('بازیابی کلمه عبور', user.email, {'user': user}, 'emails/forgot_password.html')
                return redirect(reverse('home_module:home'))

        context = {'forgot_pass_form': forgot_pass_form}
        return render(request, 'account_module/forget_pass.html', context)




class ResetPassword(View):
    def get(self, request , active_code):
        user = User.objects.filter(email_active_code=active_code).first()
        if user is None:
            return redirect(reverse('account_module:login_page'))

        reset_pass_form = ResetPasswordForm()
        context = {'reset_pass_form': reset_pass_form,'user': user}
        return render(request, 'account_module/reset_pass.html', context)

    def post(self, request , active_code):
        reset_pass_form = ResetPasswordForm(request.POST)
        if reset_pass_form.is_valid():
            user = User.objects.filter(email_active_code=active_code).first()
            if user is None:
                return redirect(reverse('account_module:login_page'))
            user_new_password = reset_pass_form.cleaned_data.get('password')
            user.set_password(user_new_password)
            user.email_active_code = get_random_string(72)
            user.is_active = True
            user.save()
            return redirect(reverse('account_module:login_page'))



class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('home_module:home'))


