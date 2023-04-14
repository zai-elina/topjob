from django import forms
from .models import *

class DateInput(forms.DateInput):
    input_type = 'date'

class SearchForm(forms.ModelForm):
    FULL_TIME = 'Полный'
    PART_TIME = 'Неполный'
    REMOTE = 'Удаленно'
    TYPE_CHOICES = [
        (FULL_TIME, 'Полная'),
        (PART_TIME, 'Неполная'),
        (REMOTE, 'Удаленно'),
    ]
    REGION = [('Республика Адыгея', 'Республика Адыгея'), ('Республика Алтай', 'Республика Алтай'),
              ('Республика Башкортостан', 'Республика Башкортостан'), ('Республика Бурятия', 'Республика Бурятия'),
              ('Республика Дагестан', 'Республика Дагестан'), ('Республика Ингушетия', 'Республика Ингушетия'),
              ('Кабардино-БалкарскаяРеспублика Республика', 'Кабардино-БалкарскаяРеспублика Республика'),
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


    title = forms.CharField(required=True,widget=forms.TextInput(attrs={'class': 'form-control form-control-lg','placeholder':'Вакансия, название компании'}))
    type = forms.ChoiceField(choices=TYPE_CHOICES, widget=forms.Select(attrs={'class':'selectpicker bg-white p-2 rounded','title':'Форма занятости'}))
    region = forms.ChoiceField(choices=REGION, widget=forms.Select(attrs={'class':'selectpicker bg-white p-2 rounded','title':'Регион','id':'selectorreg'}))
    class Meta:
        model = Jobs
        fields = ['title','type','region']

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.fields['type'].required = False
        self.fields['region'].required = False


class CompanyForm(forms.ModelForm):
    title = forms.CharField(required=True,widget=forms.TextInput(attrs={'class': 'form-control form-control-lg','placeholder':'Название компании'}))
    description = forms.CharField(required=True, widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Описание компании'}))
    companyLogo = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class':'form-control'}))

    class Meta:
        model = Company
        fields = ['title','description','companyLogo']


class JobForm(forms.ModelForm):
    FULL_TIME='Полный'
    PART_TIME='Неполный'
    REMOTE='Удаленно'
    TIER1 = 'Меньше 2 лет'
    TIER2 = '2-5 лет'
    TIER3 = '5-10 лет'
    TIER4 = '10-15 лет'
    TIER5 = '>15 лет'

    TYPE_CHOICES=[
        (FULL_TIME,'Полная'),
        (PART_TIME,'Неполная'),
        (REMOTE, 'Удаленно'),
    ]
    EXP_CHOICES=[
        (TIER1, 'Меньше 2 лет'),
        (TIER2, 'от 2 до 5 лет'),
        (TIER3, 'от 5 до 10 лет'),
        (TIER4, 'от 10 до 15 лет'),
        (TIER5, 'Больше 15 лет'),
    ]
    REGION = [('Республика Адыгея', 'Республика Адыгея'), ('Республика Алтай', 'Республика Алтай'),
              ('Республика Башкортостан', 'Республика Башкортостан'), ('Республика Бурятия', 'Республика Бурятия'),
              ('Республика Дагестан', 'Республика Дагестан'), ('Республика Ингушетия', 'Республика Ингушетия'),
              ('Кабардино-БалкарскаяРеспублика Республика', 'Кабардино-БалкарскаяРеспублика Республика'),
              ('Калмыкия Карачаево-Черкесская Республика', 'Калмыкия Карачаево-Черкесская Республика'),
              ('Республика Карелия', 'Республика Карелия'), ('Республика Коми', 'Республика Коми'),
              ('Республика Марий Эл', 'Республика Марий Эл'), ('Республика Мордовия', 'Республика Мордовия'),
              ('Республика Саха', 'Республика Саха'), ('Республика Северная Осетия-Алания', 'Республика Северная Осетия-Алания'),
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
              ('Томская область', 'Томская область'), ('Тверская область', 'Тверская область'), ('Тульская область', 'Тульская область'),
              ('Тюменская область', 'Тюменская область'), ('Ульяновская область', 'Ульяновская область'), ('Владимирская область', 'Владимирская область'),
              ('Волгоградская область', 'Волгоградская область'), ('Вологодская область', 'Вологодская область'), ('Ярославская область', 'Ярославская область'),
              ('Ненецкий автономный округ', 'Ненецкий автономный округ'), ('Ханты-Мансийский автономный округ', 'Ханты-Мансийский автономный округ'),
              ('Чукотский автономный округ', 'Чукотский автономный округ'), ('Ямало-Ненецкий автономный округ', 'Ямало-Ненецкий автономный округ')]

    title = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control resume', 'placeholder': 'Название вакансии'}))

    category =forms.ModelChoiceField(queryset=Category.objects.all(),
                                      required=True)

    city = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control resume', 'placeholder': 'Город'}))
    region = forms.ChoiceField(choices=REGION, widget=forms.Select(attrs={'class': 'nice-select rounded'}))
    salary = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control resume'}))
    type = forms.ChoiceField(choices=TYPE_CHOICES, widget=forms.Select(attrs={'class': 'nice-select rounded'}))
    experience = forms.ChoiceField(choices=EXP_CHOICES, widget=forms.Select(attrs={'class': 'nice-select rounded'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    requirements = forms.CharField( widget=forms.Textarea(attrs={'class':'form-control'}))
    duties = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    note = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    closingDate = forms.DateField(required=True, widget=DateInput(
        attrs={'class': 'form-control', 'placeholder': 'Введите дату закрытия вакансии:'}))



    class Meta:
        model = Jobs
        fields = ['title','category','city','region' ,'salary','type' ,'experience','description'  ,
                  'requirements'  ,'duties','note','closingDate',
        ]

    def __init__(self, *args, **kwargs):
        super(JobForm, self).__init__(*args, **kwargs)
        self.fields['summary'].required = False
        self.fields['note'].required = False

class ApplyJobForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = ('job',)
