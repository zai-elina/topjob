from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify
from uuid import uuid4

class Company(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    uniqueId = models.CharField(max_length=100, null=True, blank=True)
    companyLogo = models.ImageField(default='default.png',upload_to='company_logo')
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
    categoryImage = models.ImageField(default='category.png',upload_to='category-image')
    slug = models.SlugField(null=True, blank=True, unique=True, max_length=500)
    seoDescription = models.CharField(null=True, blank=True, max_length=500)
    seoKeywords = models.CharField(null=True, blank=True, max_length=500)

    def __str__(self):
        return '{} - {}'.format(self.title,self.uniqueId)

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

    title = models.CharField(max_length=200,null=True,blank=True)
    company = models.ForeignKey(Company,on_delete =models.CASCADE, null=True,blank=True)
    category = models.ForeignKey(Category,on_delete =models.CASCADE, null=True,blank=True)
    location = models.CharField(max_length=200,null=True,blank=True)
    salary = models.CharField(max_length=100,null=True,blank=True)
    uniqueId = models.CharField(max_length=100,null=True,blank=True)
    type = models.CharField(max_length=100,choices=TYPE_CHOICES, default=FULL_TIME)
    experience = models.CharField(max_length=100, choices=EXP_CHOICES, default=TIER1)
    summary = models.TextField(null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    requirements = models.TextField(null=True,blank=True)
    duties = models.TextField(null=True,blank=True)
    enquiries = models.TextField(null=True, blank=True)
    applications = models.TextField(null=True,blank=True)
    note = models.TextField(null=True,blank=True)
    dateCreated = models.DateTimeField(default=timezone.now)
    closingDate = models.DateField(null=True,blank=True)
    datePosted = models.DateField(null=True,blank=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    slug = models.SlugField(null=True,blank=True,unique=True,max_length=500)
    seoDescription = models.CharField(null=True,blank=True,max_length=500)
    seoKeywords = models.CharField(null=True,blank=True,max_length=500)
    urlLink = models.CharField(null=True,blank=True,max_length=500)

    def __str__(self):
        return '{} - {} - {}'.format(self.company,self.title,self.location)

    class Meta:
        verbose_name ="Вакансия"
        verbose_name_plural = "Вакансии"

    def get_absolute_url(self):
        return reversed('job-detail',kwargs={'slug':self.slug})

    def save(self,*args,**kwargs):
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[0]
            self.slug = slugify('{} {} {}'.format(self.title,self.location,self.uniqueId))

        self.slug = slugify('{} {} {}'.format(self.title,self.location,self.uniqueId))
        self.seoKeywords = 'портал по поиску работы, удаленная работа, поиск работы, найти работу, устроиться на работу, {}'.format(self.title)
        self.seoDescription = 'Подать онлайн заявку на работу в {}'.format(self.title)
        super(Jobs,self).save(*args,**kwargs)



