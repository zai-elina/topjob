from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

from .models import Resume,Education,Experience


class DateInput(forms.DateInput):
    input_type = 'date'


# Создаём класс формы для регистрации
class RegisterForm(UserCreationForm):
    KIND = [
        ('Соискатель', 'Соискатель'),
        ('Работодатель', 'Работодатель'),
    ]

    image = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'form-control'}))

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

    kind = forms.ChoiceField(required=True,choices=KIND, widget=forms.Select(attrs={'class':'nice-select rounded'}))

    class Meta:
        # Свойство модели User
        model = User
        # Свойство назначения полей
        fields = ('image','username','first_name', 'last_name','email', 'password1', 'password2','kind')


class ProfileChangeForm(UserChangeForm):
    image = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=100,
                             required=True,
                             help_text='Введите почту',
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100,
                                 required=True,
                                 help_text='Введите имя',
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100,
                                required=True,
                                help_text='Введите фамилию',
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=200,
                               required=True,
                               help_text='Логин',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ('image','username','first_name', 'last_name','email')


class ResumeForm(forms.ModelForm):
    REGION = [('Республика Адыгея', 'Республика Адыгея'), ('Республика Алтай', 'Республика Алтай'),
              ('Республика Башкортостан', 'Республика Башкортостан'), ('Республика Бурятия', 'Республика Бурятия'),
              ('Республика Дагестан', 'Республика Дагестан'), ('Республика Ингушетия', 'Республика Ингушетия'),
              ('Кабардино-Балкарская Республика', 'Кабардино-Балкарская Республика'),
              ('Калмыкия Карачаево-Черкесская Республика', 'Калмыкия Карачаево-Черкесская Республика'),
              ('Республика Карелия', 'Республика Карелия'), ('Республика Коми', 'Республика Коми'),
              ('Республика Марий Эл', 'Республика Марий Эл'), ('Республика Мордовия', 'Республика Мордовия'),
              ('Республика Саха', 'Республика Саха'),
              ('Республика Северная Осетия-Алания', 'Республика Северная Осетия-Алания'),
              ('Республика Татарстан', 'Республика Татарстан'), ('Республика Тыва', 'Республика Тыва'),
              ('Удмуртская Республика', 'Удмуртская Республика'), ('Республика Хакасия', 'Республика Хакасия'),
              ('Чеченская Республика', 'Чеченская Республика'), ('Чувашская Республика', 'Чувашская Республика'),
              ('Республика Крым', 'Республика Крым'), ('Амурская область', 'Амурская область'),
              ('Архангельская область', 'Архангельская область'), ('Астраханская область', 'Астраханская область'),
              ('Белгородская область', 'Белгородская область'), ('Брянская область', 'Брянская область'),
              ('Челябинская область', 'Челябинская область'), ('Воронежская область', 'Воронежская область'),
              ('Иркутская область', 'Иркутская область'), ('Ивановская область', 'Ивановская область'),
              ('Калининградская область', 'Калининградская область'), ('Калужская область', 'Калужская область'),
              ('Кемеровская область', 'Кемеровская область'), ('Кировская область', 'Кировская область'),
              ('Костромская область', 'Костромская область'), ('Курганская область', 'Курганская область'),
              ('Курская область', 'Курская область'), ('Ленинградская область', 'Ленинградская область'),
              ('Липецкая область', 'Липецкая область'), ('Магаданская область', 'Магаданская область'),
              ('Московская область', 'Московская область'), ('Мурманская область', 'Мурманская область'),
              ('Нижегородская область', 'Нижегородская область'), ('Новгородская область', 'Новгородская область'),
              ('Новосибирская область', 'Новосибирская область'), ('Омская область', 'Омская область'),
              ('Оренбургская область', 'Оренбургская область'), ('Орловская область', 'Орловская область'),
              ('Пензенская область', 'Пензенская область'), ('Псковская область', 'Псковская область'),
              ('Ростовская область', 'Ростовская область'), ('Рязанская область', 'Рязанская область'),
              ('Сахалинская область', 'Сахалинская область'), ('Самарская область', 'Самарская область'),
              ('Саратовская область', 'Саратовская область'), ('Смоленская область', 'Смоленская область'),
              ('Свердловская область', 'Свердловская область'), ('Тамбовская область', 'Тамбовская область'),
              ('Томская область', 'Томская область'), ('Тверская область', 'Тверская область'),
              ('Тульская область', 'Тульская область'), ('Тюменская область', 'Тюменская область'),
              ('Ульяновская область', 'Ульяновская область'), ('Владимирская область', 'Владимирская область'),
              ('Волгоградская область', 'Волгоградская область'), ('Вологодская область', 'Вологодская область'),
              ('Ярославская область', 'Ярославская область'), ('Амурская область', 'Амурская область'),
              ('Архангельская областьАстраханская область', 'Архангельская областьАстраханская область'),
              ('Белгородская область', 'Белгородская область'), ('Брянская область', 'Брянская область'),
              ('Челябинская область', 'Челябинская область'), ('Воронежская область', 'Воронежская область'),
              ('Иркутская область', 'Иркутская область'), ('Ивановская область', 'Ивановская область'),
              ('Калининградская область', 'Калининградская область'), ('Калужская область', 'Калужская область'),
              ('Кемеровская область', 'Кемеровская область'), ('Кировская область', 'Кировская область'),
              ('Костромская область', 'Костромская область'), ('Курганская область', 'Курганская область'),
              ('Курская область', 'Курская область'), ('Ленинградская область', 'Ленинградская область'),
              ('Липецкая область', 'Липецкая область'), ('Магаданская область', 'Магаданская область'),
              ('Московская область', 'Московская область'), ('Мурманская область', 'Мурманская область'),
              ('Нижегородская область', 'Нижегородская область'), ('Новгородская область', 'Новгородская область'),
              ('Новосибирская область', 'Новосибирская область'), ('Омская область', 'Омская область'),
              ('Оренбургская область', 'Оренбургская область'), ('Орловская область', 'Орловская область'),
              ('Пензенская область', 'Пензенская область'), ('Псковская область', 'Псковская область'),
              ('Ростовская область', 'Ростовская область'), ('Рязанская область', 'Рязанская область'),
              ('Сахалинская область', 'Сахалинская область'), ('Самарская область', 'Самарская область'),
              ('Саратовская область', 'Саратовская область'), ('Смоленская область', 'Смоленская область'),
              ('Свердловская область', 'Свердловская область'), ('Тамбовская область', 'Тамбовская область'),
              ('Томская область', 'Томская область'), ('Тверская область', 'Тверская область'),
              ('Тульская область', 'Тульская область'),
              ('Тюменская область', 'Тюменская область'), ('Ульяновская область', 'Ульяновская область'),
              ('Владимирская область', 'Владимирская область'),
              ('Волгоградская область', 'Волгоградская область'), ('Вологодская область', 'Вологодская область'),
              ('Ярославская область', 'Ярославская область'),
              ('Ненецкий автономный округ', 'Ненецкий автономный округ'),
              ('Ханты-Мансийский автономный округ', 'Ханты-Мансийский автономный округ'),
              ('Чукотский автономный округ', 'Чукотский автономный округ'),
              ('Ямало-Ненецкий автономный округ', 'Ямало-Ненецкий автономный округ')]
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


    date_birth = forms.DateField(required=True, widget=DateInput(attrs={'class':'form-control','placeholder':'Введите дату рождения:'}))
    sex = forms.ChoiceField(choices=SEX_CHOICES, widget=forms.Select(attrs={'class':'nice-select rounded'}))
    material_status =forms.ChoiceField(choices=MATERIAL_CHOICES,widget=forms.Select(attrs={'class':'nice-select rounded'}))
    addressLine1 = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control resume','placeholder':'Введите адрес проживания:'}))
    addressLine2 = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control resume','placeholder':'Введите адрес прописки:'}))
    suburb = forms.ChoiceField(choices=REGION, widget=forms.Select(attrs={'class':'selectpicker bg-white p-2 rounded','title':'Регион','id':'selectorreg'}))
    city = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control resume','placeholder':'Введите город:'}))
    phoneNumber =forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control resume','placeholder':'Введите номер телефона:'}))
    cover_letter =forms.FileField(required=False,widget=forms.FileInput(attrs={'class':'form-control'}))
    cv = forms.FileField(required=False,widget=forms.FileInput(attrs={'class':'form-control'}))
    skills = forms.CharField(required=True,
                             widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ваши навыки'}))


    class Meta:
        model = Resume
        fields=[
            'date_birth','sex','material_status','addressLine1',
            'addressLine2','suburb','city','phoneNumber', 'cover_letter','cv','skills'
        ]

class ResumeEditForm(forms.ModelForm):
    REGION = [('Республика Адыгея', 'Республика Адыгея'), ('Республика Алтай', 'Республика Алтай'),
              ('Республика Башкортостан', 'Республика Башкортостан'), ('Республика Бурятия', 'Республика Бурятия'),
              ('Республика Дагестан', 'Республика Дагестан'), ('Республика Ингушетия', 'Республика Ингушетия'),
              ('Кабардино-Балкарская Республика', 'Кабардино-Балкарская Республика'),
              ('Калмыкия Карачаево-Черкесская Республика', 'Калмыкия Карачаево-Черкесская Республика'),
              ('Республика Карелия', 'Республика Карелия'), ('Республика Коми', 'Республика Коми'),
              ('Республика Марий Эл', 'Республика Марий Эл'), ('Республика Мордовия', 'Республика Мордовия'),
              ('Республика Саха', 'Республика Саха'),
              ('Республика Северная Осетия-Алания', 'Республика Северная Осетия-Алания'),
              ('Республика Татарстан', 'Республика Татарстан'), ('Республика Тыва', 'Республика Тыва'),
              ('Удмуртская Республика', 'Удмуртская Республика'), ('Республика Хакасия', 'Республика Хакасия'),
              ('Чеченская Республика', 'Чеченская Республика'), ('Чувашская Республика', 'Чувашская Республика'),
              ('Республика Крым', 'Республика Крым'), ('Амурская область', 'Амурская область'),
              ('Архангельская область', 'Архангельская область'), ('Астраханская область', 'Астраханская область'),
              ('Белгородская область', 'Белгородская область'), ('Брянская область', 'Брянская область'),
              ('Челябинская область', 'Челябинская область'), ('Воронежская область', 'Воронежская область'),
              ('Иркутская область', 'Иркутская область'), ('Ивановская область', 'Ивановская область'),
              ('Калининградская область', 'Калининградская область'), ('Калужская область', 'Калужская область'),
              ('Кемеровская область', 'Кемеровская область'), ('Кировская область', 'Кировская область'),
              ('Костромская область', 'Костромская область'), ('Курганская область', 'Курганская область'),
              ('Курская область', 'Курская область'), ('Ленинградская область', 'Ленинградская область'),
              ('Липецкая область', 'Липецкая область'), ('Магаданская область', 'Магаданская область'),
              ('Московская область', 'Московская область'), ('Мурманская область', 'Мурманская область'),
              ('Нижегородская область', 'Нижегородская область'), ('Новгородская область', 'Новгородская область'),
              ('Новосибирская область', 'Новосибирская область'), ('Омская область', 'Омская область'),
              ('Оренбургская область', 'Оренбургская область'), ('Орловская область', 'Орловская область'),
              ('Пензенская область', 'Пензенская область'), ('Псковская область', 'Псковская область'),
              ('Ростовская область', 'Ростовская область'), ('Рязанская область', 'Рязанская область'),
              ('Сахалинская область', 'Сахалинская область'), ('Самарская область', 'Самарская область'),
              ('Саратовская область', 'Саратовская область'), ('Смоленская область', 'Смоленская область'),
              ('Свердловская область', 'Свердловская область'), ('Тамбовская область', 'Тамбовская область'),
              ('Томская область', 'Томская область'), ('Тверская область', 'Тверская область'),
              ('Тульская область', 'Тульская область'), ('Тюменская область', 'Тюменская область'),
              ('Ульяновская область', 'Ульяновская область'), ('Владимирская область', 'Владимирская область'),
              ('Волгоградская область', 'Волгоградская область'), ('Вологодская область', 'Вологодская область'),
              ('Ярославская область', 'Ярославская область'), ('Амурская область', 'Амурская область'),
              ('Архангельская областьАстраханская область', 'Архангельская областьАстраханская область'),
              ('Белгородская область', 'Белгородская область'), ('Брянская область', 'Брянская область'),
              ('Челябинская область', 'Челябинская область'), ('Воронежская область', 'Воронежская область'),
              ('Иркутская область', 'Иркутская область'), ('Ивановская область', 'Ивановская область'),
              ('Калининградская область', 'Калининградская область'), ('Калужская область', 'Калужская область'),
              ('Кемеровская область', 'Кемеровская область'), ('Кировская область', 'Кировская область'),
              ('Костромская область', 'Костромская область'), ('Курганская область', 'Курганская область'),
              ('Курская область', 'Курская область'), ('Ленинградская область', 'Ленинградская область'),
              ('Липецкая область', 'Липецкая область'), ('Магаданская область', 'Магаданская область'),
              ('Московская область', 'Московская область'), ('Мурманская область', 'Мурманская область'),
              ('Нижегородская область', 'Нижегородская область'), ('Новгородская область', 'Новгородская область'),
              ('Новосибирская область', 'Новосибирская область'), ('Омская область', 'Омская область'),
              ('Оренбургская область', 'Оренбургская область'), ('Орловская область', 'Орловская область'),
              ('Пензенская область', 'Пензенская область'), ('Псковская область', 'Псковская область'),
              ('Ростовская область', 'Ростовская область'), ('Рязанская область', 'Рязанская область'),
              ('Сахалинская область', 'Сахалинская область'), ('Самарская область', 'Самарская область'),
              ('Саратовская область', 'Саратовская область'), ('Смоленская область', 'Смоленская область'),
              ('Свердловская область', 'Свердловская область'), ('Тамбовская область', 'Тамбовская область'),
              ('Томская область', 'Томская область'), ('Тверская область', 'Тверская область'),
              ('Тульская область', 'Тульская область'),
              ('Тюменская область', 'Тюменская область'), ('Ульяновская область', 'Ульяновская область'),
              ('Владимирская область', 'Владимирская область'),
              ('Волгоградская область', 'Волгоградская область'), ('Вологодская область', 'Вологодская область'),
              ('Ярославская область', 'Ярославская область'),
              ('Ненецкий автономный округ', 'Ненецкий автономный округ'),
              ('Ханты-Мансийский автономный округ', 'Ханты-Мансийский автономный округ'),
              ('Чукотский автономный округ', 'Чукотский автономный округ'),
              ('Ямало-Ненецкий автономный округ', 'Ямало-Ненецкий автономный округ')]
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


    sex = forms.ChoiceField(choices=SEX_CHOICES, widget=forms.Select(attrs={'class':'nice-select rounded'}))
    material_status =forms.ChoiceField(choices=MATERIAL_CHOICES,widget=forms.Select(attrs={'class':'nice-select rounded'}))
    addressLine1 = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control resume','placeholder':'Введите адрес проживания:'}))
    addressLine2 = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control resume','placeholder':'Введите адрес прописки:'}))
    suburb = forms.ChoiceField(choices=REGION, widget=forms.Select(attrs={'class':'selectpicker bg-white p-2 rounded','title':'Регион','id':'selectorreg'}))
    city = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control resume','placeholder':'Введите город:'}))
    phoneNumber =forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control resume','placeholder':'Введите номер телефона:'}))
    cover_letter =forms.FileField(required=False,widget=forms.FileInput(attrs={'class':'form-control'}))
    cv = forms.FileField(required=False,widget=forms.FileInput(attrs={'class':'form-control'}))
    skills = forms.CharField(required=True,
                             widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ваши навыки'}))


    class Meta:
        model = Resume
        fields=[
            'sex','material_status','addressLine1',
            'addressLine2','suburb','city','phoneNumber', 'cover_letter','cv', 'skills'
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
    faculty = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Факультет'}))
    level = forms.ChoiceField(choices=LEVEL_CHOICES, widget=forms.Select(attrs={'class':'nice-select rounded'}))
    start_date = forms.DateField(required=True, widget=DateInput(attrs={'class':'form-control','placeholder':'Дата начала'}))
    graduated = forms.DateField(required=True, widget=DateInput(attrs={'class':'form-control','placeholder':'Дата окончания обучения'}))
    specialization = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Специализация'}))

    class Meta:
        model = Education
        fields = [
            'institution' ,'faculty' ,'level','start_date' ,'graduated' ,'specialization',
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


class LoginForm(forms.Form):
    username = forms.CharField(max_length=200,
                               required=True,
                               help_text='Логин',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Логин'}))
    password = forms.CharField(
        required=True,
        help_text='Введите пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}))

    class Meta:
        model =User
        fields =['username','password']
