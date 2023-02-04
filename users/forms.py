from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Создаём класс формы
class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=100,
                             required=True,
                             help_text='Введите почту',
                             widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Почта'}))
    first_name = forms.CharField(max_length=100,
                                 required=True,
                                 help_text='Введите имя',
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваше имя'}))
    last_name = forms.CharField(max_length=100,
                                required=True,
                                help_text='Введите фамилию',
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваша фамилия'}))
    username = forms.CharField(max_length=200,
                                required=True,
                                help_text='Логин',
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Логин'}))
    password1 = forms.CharField(
                               required=True,
                               help_text='Введите пароль',
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}))
    password2 = forms.CharField(
                                required=True,
                                help_text='Введите пароль ещё раз',
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Повторный пароль'}))

    class Meta:
        # Свойство модели User
        model = User
        # Свойство назначения полей
        fields = ('username','first_name', 'last_name','email', 'password1', 'password2',)