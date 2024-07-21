from django import forms
from django.core import validators
from django.core.exceptions import ValidationError

class RegisterForm(forms.Form):
    email = forms.EmailField(label='ایمیل' , widget=forms.EmailInput(attrs={'class':'form-control', 'id':'email'}), validators=[validators.validate_email , validators.MaxLengthValidator(100)])
    password = forms.CharField(label='کلمه عبور',widget=forms.PasswordInput(attrs={'class':'form-control','id':'password'}) , validators=[validators.MaxLengthValidator(100)])
    confirm_password = forms.CharField(label='تکرار کلمه عبور',widget=forms.PasswordInput(attrs={'class':'form-control','id':'confirm_password'}), validators=[validators.MaxLengthValidator(100)])

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password == confirm_password:
            return confirm_password
        raise ValidationError('کلمه عبور و تکرار کلمه عبور مغایرت دارند')



class LoginForm(forms.Form):
    email = forms.EmailField(label='ایمیل', widget=forms.EmailInput(attrs={'class': 'form-control', 'id': 'email'}),validators=[validators.validate_email, validators.MaxLengthValidator(100)])
    password = forms.CharField(label='کلمه عبور',widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'password'}),validators=[validators.MaxLengthValidator(100)])


class ForgotForm(forms.Form):
    email = forms.EmailField(label='ایمیل', widget=forms.EmailInput(attrs={'class': 'form-control', 'id': 'email'}),validators=[validators.validate_email, validators.MaxLengthValidator(100)])


class ResetPasswordForm(forms.Form):
    password = forms.CharField(label='کلمه عبور',widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'password'}),validators=[validators.MaxLengthValidator(100)])
    confirm_password = forms.CharField(label='تکرار کلمه عبور', widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'confirm_password'}), validators=[validators.MaxLengthValidator(100)])
