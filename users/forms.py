from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Resume,Education,Experience


class DateInput(forms.DateInput):
    input_type = 'date'


# Создаём класс формы для регистрации
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



class ResumeForm(forms.ModelForm):
    MALE = 'Мужчина'
    FEMALE = 'Женщина'
    OTHER = 'Другое'
    MARRIED = 'Женат/Замужем'
    SINGLE = 'Одинок(а)'
    WIDOWED = 'Вдовец/Вдова'
    DIVORCED = 'Разведён(а)'

    SEX_CHOICES = [
        (MALE, 'Мужчина'),
        (FEMALE, 'Женщина'),
        (OTHER, 'Другое'),
    ]
    MATERIAL_CHOICES = [
        (MARRIED, 'Женат/Замужем'),
        (SINGLE, 'Одинок(а)'),
        (WIDOWED, 'Вдовец/Вдова'),
        (DIVORCED, 'Разведён(а)'),
    ]

    image = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class':'form-control'}))
    date_birth = forms.DateField(required=True, widget=DateInput(attrs={'class':'form-control','placeholder':'Введите дату рождения:'}))
    sex = forms.ChoiceField(choices=SEX_CHOICES, widget=forms.Select(attrs={'class':'nice-select rounded'}))
    material_status =forms.ChoiceField(choices=MATERIAL_CHOICES,widget=forms.Select(attrs={'class':'nice-select rounded'}))
    addressLine1 = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control resume','placeholder':'Введите адрес проживания:'}))
    addressLine2 = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control resume','placeholder':'Введите адрес прописки:'}))
    suburb = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control resume','placeholder':'Введите название республики, области или края:'}))
    city = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control resume','placeholder':'Введите город:'}))
    phoneNumber =forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control resume','placeholder':'Введите номер телефона:'}))
    cover_letter =forms.FileField(required=False,widget=forms.FileInput(attrs={'class':'form-control'}))
    cv = forms.FileField(required=False,widget=forms.FileInput(attrs={'class':'form-control'}))


    class Meta:
        model = Resume
        fields=[
            'image','date_birth','sex','material_status','addressLine1',
            'addressLine2','suburb','city','phoneNumber', 'cover_letter','cv',
        ]
class EducationForm(forms.ModelForm):
    LEVEL1 = 'Среднее образование'
    LEVEL2 = 'Среднее профессиональное образование'
    LEVEL3 = 'Бакалавриат высшего образования'
    LEVEL4 = 'Специалитет высшего образования'
    LEVEL5 = 'Магистратура высшего образования'
    LEVEL6 = 'Аспирантура'
    LEVEL7 = 'Докторская степень'
    LEVEL8 = 'Сертификат'

    LEVEL_CHOICES = [
        (LEVEL1, 'Среднее образование'),
        (LEVEL2, 'Среднее профессиональное образование'),
        (LEVEL3, 'Бакалавриат высшего образования'),
        (LEVEL4, 'Специалитет высшего образования'),
        (LEVEL5, 'Магистратура высшего образования'),
        (LEVEL6, 'Аспирантура'),
        (LEVEL7, 'Докторская степень'),
        (LEVEL8, 'Сертификат'),
    ]

    institution = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Название учебного заведения'}))
    qualification = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Квалификация'}))
    level = forms.ChoiceField(choices=LEVEL_CHOICES, widget=forms.Select(attrs={'class':'nice-select rounded'}))
    start_date = forms.DateField(required=True, widget=DateInput(attrs={'class':'form-control','placeholder':'Дата начала'}))
    graduated = forms.DateField(required=True, widget=DateInput(attrs={'class':'form-control','placeholder':'Дата окончания обучения'}))
    direction = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Название вашего направления'}))

    class Meta:
        model = Education
        fields = [
            'institution' ,'qualification' ,'level','start_date' ,'graduated' ,'direction',
        ]

class ExperienceForm(forms.ModelForm):
    company = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Компания, в которой работали'}))
    position = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Должность'}))
    start_date = forms.DateField(required=True, widget=DateInput(attrs={'class':'form-control','placeholder':'Дата начала'}))
    end_date = forms.DateField(required=True, widget=DateInput(attrs={'class':'form-control','placeholder':'Дата конца'}))
    experience =forms.CharField(required=True, widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Опишите свой опыт'}))
    skills = forms.CharField(required=True, widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Ваши навыки'}))

    class Meta:
        model = Experience
        fields = [
            'company' ,'position' ,'start_date' ,'end_date' ,'experience' ,'skills',
        ]

class ForgotForm(forms.ModelForm):
    email = forms.EmailField(max_length=100,
                             required=True,
                             help_text='Введите почту',
                             widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Почта'}))

    class Meta:
        model =User
        fields =['email',]
