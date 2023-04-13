from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from uuid import uuid4
from django.urls import reverse
import random
from django.template.defaultfilters import slugify as django_slugify

from jobs.models import Jobs

alphabet = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i',
            'й': 'j', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
            'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ы': 'i', 'э': 'e', 'ю': 'yu',
            'я': 'ya'}


def slugify(s):
    """
    Overriding django slugify that allows to use russian words as well.
    """
    return django_slugify(''.join(alphabet.get(w, w) for w in s.lower()))


class Profile(models.Model):
    KIND = [
        ('Соискатель', 'Соискатель'),
        ('Работодатель', 'Работодатель'),
    ]

    IMAGES = [
        'profile1.jpg', 'profile2.jpg', 'profile3.jpg', 'profile4.jpg', 'profile5.jpg',
        'profile6.jpg', 'profile7.jpg', 'profile8.jpg',
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    kind = models.CharField(choices=KIND,default='Соискатель',max_length=30)
    slug = models.SlugField(unique=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_image')
    uniqueId = models.CharField(null=True, max_length=100, blank=True)

    def save(self,*args,**kwargs):
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[0]
            self.slug = slugify('{} {}'.format(self.user.username, self.uniqueId))

        self.slug = slugify('{} {}'.format(self.user.username, self.uniqueId))

            # фото профиля по умолчанию
        if self.image == 'default.jpg':
            self.image = random.choice(self.IMAGES)

        super(Profile,self).save(*args,**kwargs)

    class Meta:
        verbose_name ="Профиль"
        verbose_name_plural = "Профили"

class Resume(models.Model):
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

    MALE = 'Мужчина'
    FEMALE = 'Женщина'
    OTHER = 'Другое'
    MARRIED ='Женат/Замужем'
    SINGLE = 'Одинок(а)'
    WIDOWED ='Вдовец/Вдова'
    DIVORCED ='Разведён(а)'

    SEX_CHOICES = [
        (MALE , 'Мужчина'),
        (FEMALE , 'Женщина'),
        (OTHER , 'Другое'),
    ]
    MATERIAL_CHOICES = [
        (MARRIED, 'Женат/Замужем'),
        (SINGLE, 'Одинок(а)'),
        (WIDOWED, 'Вдовец/Вдова'),
        (DIVORCED,'Разведён(а)'),
    ]



    user = models.OneToOneField(User, on_delete = models.CASCADE)
    profession = models.CharField(null=True, max_length=100,blank=True)
    uniqueId = models.CharField(null=True, max_length=100,blank=True)
    email_confirmed = models.BooleanField(default=False)
    date_birth  = models.DateField(blank=True,null=True)
    sex = models.CharField(choices=SEX_CHOICES, default=OTHER,max_length=100)
    material_status = models.CharField(choices=MATERIAL_CHOICES, default=SINGLE,max_length=100)
    addressLine1 = models.CharField(null=True,max_length=200,blank=True)
    addressLine2 = models.CharField(null=True,max_length=200,blank=True)
    suburb = models.CharField(choices=REGION,max_length=100)
    city = models.CharField(null=True,blank=True,max_length=100)
    phoneNumber = models.CharField(null=True,blank=True,max_length=100)
    slug = models.SlugField(max_length=500,unique=True,blank=True,null=True)
    date_created = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(blank=True,null=True)
    cv = models.FileField(upload_to='resumes',null=True,blank=True)
    skills = models.TextField()

    def __str__(self):
        return '{} {} {}'.format(self.user.first_name,self.user.last_name, self.uniqueId)

    def get_absolute_url(self):
        return reverse('resume-detail', kwargs={'slug':self.slug})

    def save(self,*args,**kwargs):
        # Создание уникального идентификатора резюме
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[0]
            self.slug = slugify('{} {} {}'.format(self.user.first_name, self.user.last_name, self.uniqueId))



        self.slug = slugify('{} {} {}'.format(self.user.first_name, self.user.last_name, self.uniqueId))

        super(Resume,self).save(*args,**kwargs)


    class Meta:
        verbose_name ="Резюме"
        verbose_name_plural = "Резюме"


class Education(models.Model):
    LEVEL1 = 'Среднее образование'
    LEVEL2 = 'Среднее профессиональное образование'
    LEVEL3 = 'Бакалавриат высшего образования'
    LEVEL4 = 'Специалитет высшего образования'
    LEVEL5 = 'Магистратура высшего образования'
    LEVEL6 = 'Аспирантура'
    LEVEL7 = 'Докторская степень'
    LEVEL8 = 'Сертификат'

    LEVEL_CHOICES = [
        (LEVEL1 , 'Среднее образование'),
        (LEVEL2 , 'Среднее профессиональное образование'),
        (LEVEL3 , 'Бакалавриат высшего образования'),
        (LEVEL4 , 'Специалитет высшего образования'),
        (LEVEL5 , 'Магистратура высшего образования'),
        (LEVEL6 , 'Аспирантура'),
        (LEVEL7 , 'Докторская степень'),
        (LEVEL8 , 'Сертификат'),
    ]

    institution = models.CharField(max_length=200,null=True)
    faculty = models.CharField(null=True,max_length=200)
    level = models.CharField(choices=LEVEL_CHOICES,default=LEVEL1,max_length=200)
    start_date = models.DateField()
    graduated = models.DateField()
    specialization = models.CharField(max_length=200,null=True)
    resume = models.ForeignKey(Resume,on_delete=models.CASCADE)

    class Meta:
        verbose_name ="Образование"
        verbose_name_plural = "Образования"

    def __str__(self):
        return '{} - {} {}'.format(self.qualification,self.resume.user.first_name,self.resume.user.last_name)

class Experience(models.Model):
    company = models.CharField(null=True,max_length=200)
    position = models.CharField(null=True,max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    experience = models.TextField()
    skills = models.TextField()
    resume = models.ForeignKey(Resume,on_delete=models.CASCADE)

    def __str__(self):
        return '{} в {}'.format(self.position, self.company)
    class Meta:
        verbose_name ="Опыт работы"
        verbose_name_plural = "Опыты работы"


class Favorite(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Jobs, null=False, blank=False, on_delete=models.CASCADE)