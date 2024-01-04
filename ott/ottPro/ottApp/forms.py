from django import forms

from .models import Register



class LoginForm(forms.ModelForm):
    class Meta:
        model = Register
        exclude = ['registration_date']
        fields= ['username','fullname','email','phno','password']