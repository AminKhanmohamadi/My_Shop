from django import forms
from .models import ContactUs
class ContactForm(forms.Form):
    full_name = forms.CharField(label='Full Name', max_length=100 ,)
    email = forms.EmailField(label='Email Address' , max_length=100 , widget=forms.TextInput(attrs={'class':'form-control' , 'placeholder':'Email Address'}))
    subject = forms.CharField(label='Subject', max_length=100)
    message = forms.CharField(widget=forms.Textarea)


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ('title', 'email', 'full_name', 'message')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'input1' , 'placeholder':'موضوع پیام' }),
            'email': forms.EmailInput(attrs={'class':'input1' , 'placeholder':'پست الکترونیک شما'}),
            'full_name': forms.TextInput(attrs={'class': 'input1' , 'placeholder':'نام شما ' }),
            'message': forms.Textarea(attrs={'class':'input1' , 'placeholder':'متن پیام'})
        }
        labels = {
            'title': '',
            'email': '',
            'full_name': '',
            'message': '',
        }
        error_messages = {
            'title' : {
                'required': 'موضوع پیام را وارد کنید'
            }
        }




