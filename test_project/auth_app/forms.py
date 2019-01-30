from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


# class UserRegisterForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ('username', 'first_name', 'password1', 'password2', 'email',
#                   'au_age', 'au_avatar')
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for field_name, field in self.fields.items():
#             field.widget.attrs['class'] = 'form-control'
#             field.help_text = ''
#
#     def clean_age(self):
#         data = self.cleaned_data['age']
#         if data < 18:
#             raise forms.ValidationError("You are too young!")
#         return data


