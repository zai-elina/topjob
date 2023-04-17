from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify
from uuid import uuid4

class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True, blank=True,unique=True)
    description = models.TextField(null=True, blank=True)
    uniqueId = models.CharField(max_length=100, null=True, blank=True)
    companyLogo = models.ImageField(default='company.png',upload_to='company_logo')
    slug = models.SlugField(null=True, blank=True, unique=True, max_length=500)
    seoDescription = models.CharField(null=True, blank=True, max_length=500)
    seoKeywords = models.CharField(null=True, blank=True, max_length=500)


    def __str__(self):
        return '{} - {}'.format(self.title,self.uniqueId)

    class Meta:
        verbose_name ="Компания"
        verbose_name_plural = "Компании"

    def get_absolute_url(self):
        return reversed('company-detail',kwargs={'slug':self.slug})


    def save(self,*args,**kwargs):
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[0]
            self.slug = slugify('Company {} {}'.format(self.title,self.uniqueId))

        self.slug=slugify('Company {} {}'.format(self.title,self.uniqueId))
        self.seoKeywords = '{}, Вакансии,Подать заявку на работу, Найти работу'.format(self.title)
        self.seoDescription = 'Подать онлайн заявку на работу в {}'.format(self.title)

        super(Company,self).save(*args,**kwargs)



class Category(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    uniqueId = models.CharField(max_length=100, null=True, blank=True)
    categoryImage = models.ImageField(default='category.jpg',upload_to='category-image')
    slug = models.SlugField(null=True, blank=True, unique=True, max_length=500)
    seoDescription = models.CharField(null=True, blank=True, max_length=500)
    seoKeywords = models.CharField(null=True, blank=True, max_length=500)

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        verbose_name ="Категория"
        verbose_name_plural = "Категории"

    def get_absolute_url(self):
        return reversed('category-detail',kwargs={'slug':self.slug})


    def save(self,*args,**kwargs):
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[0]
            self.slug = slugify('Category {} {}'.format(self.title,self.uniqueId))

        self.slug=slugify('Category {} {}'.format(self.title,self.uniqueId))
        self.seoKeywords = '{}, вакансии, подать заявку на работу, найти работу'.format(self.title)
        self.seoDescription = 'Подать онлайн заявку на работу в {}'.format(self.title)
        super(Category,self).save(*args,**kwargs)


class Jobs(models.Model):
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

    title = models.CharField(max_length=200,null=True,blank=True)
    company = models.ForeignKey(Company,on_delete =models.CASCADE, null=True,blank=True)
    category = models.ForeignKey(Category,on_delete =models.CASCADE, null=True,blank=True)
    city = models.CharField(max_length=200,null=True,blank=True)
    region = models.CharField(choices=REGION,max_length=100)
    salary = models.CharField(max_length=100,null=True,blank=True)
    uniqueId = models.CharField(max_length=100,null=True,blank=True)
    type = models.CharField(max_length=100,choices=TYPE_CHOICES, default=FULL_TIME)
    experience = models.CharField(max_length=100, choices=EXP_CHOICES, default=TIER1)
    description = models.TextField(null=True,blank=True)
    requirements = models.TextField(null=True,blank=True)
    duties = models.TextField(null=True,blank=True)
    applications = models.TextField(null=True)
    note = models.TextField(null=True)
    dateCreated = models.DateTimeField(default=timezone.now)
    closingDate = models.DateField(null=True,blank=True)
    datePosted = models.DateField(null=True,blank=True)
    slug = models.SlugField(null=True,blank=True,unique=True,max_length=500)
    seoDescription = models.CharField(null=True,blank=True,max_length=500)
    seoKeywords = models.CharField(null=True,blank=True,max_length=500)
    urlLink = models.CharField(null=True,blank=True,max_length=500)
    filled = models.BooleanField(default=False)

    def __str__(self):
        return '{} - {} - {}'.format(self.company,self.title,self.region)

    class Meta:
        verbose_name ="Вакансия"
        verbose_name_plural = "Вакансии"

    def get_absolute_url(self):
        return reversed('job-detail',kwargs={'slug':self.slug})

    def save(self,*args,**kwargs):
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[0]
            self.slug = slugify('{} {} {}'.format(self.title,self.region,self.uniqueId))

        self.slug = slugify('{} {} {}'.format(self.title,self.region,self.uniqueId))
        self.seoKeywords = 'портал по поиску работы, удаленная работа, поиск работы, найти работу, устроиться на работу, {}'.format(self.title)
        self.seoDescription = 'Подать онлайн заявку на работу в {}'.format(self.title)
        super(Jobs,self).save(*args,**kwargs)


class Applicant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Jobs, on_delete=models.CASCADE, related_name='applicants')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '{} - {}'.format(self.user,self.job)

    class Meta:
        verbose_name ="Заявитель"
        verbose_name_plural = "Заявители"


