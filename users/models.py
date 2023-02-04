from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.utils import timezone
from uuid import uuid4
from django.urls import reverse
import random

class Resume(models.Model):
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
    uniqueId = models.CharField(null=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_image')
    email_confirmed = models.BooleanField(default=False)
    date_birth  = models.DateField()
    sex = models.CharField(choices=SEX_CHOICES, default=OTHER)
    material_status = models.CharField(choices=MATERIAL_CHOICES, default=SINGLE)
    addressLine1 = models.CharField(null=True)
    addressLine2 = models.CharField(null=True)
    suburb = models.CharField(null=True)
    city = models.CharField(null=True)
    phoneNumber = models.CharField(null=True)
    slug = models.SlugField(max_length=300,unique=True,blank=True,null=True)
    date_created = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField()
    cover_letter =models.FileField(upload_to='resumes')
    cv = models.FileField(upload_to='resumes')

    def __str__(self):
        return '{} {} {}'.format(self.user.first_name,self.user.last_name, self.uniqueId)

    def get_absolute_url(self):
        return reverse('resume-detail', kwargs={'slug':self.slug})