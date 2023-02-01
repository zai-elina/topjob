from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class Jobs(models.Model):
    FULL_TIME='FT'
    PART_TIME='PT'
    REMOTE='RT'
    TIER1 = 't1'
    TIER2 = 't2'
    TIER3 = 't3'
    TIER4 = 't4'
    TIER5 = 't5'

    TYPE_CHOICES=[
        (FULL_TIME,'Полная'),
        (PART_TIME,'Неполная'),
        (REMOTE, 'Удаленная'),
    ]
    EXP_CHOICES=[
        (TIER1, 'Меньше 2 лет'),
        (TIER2, 'от 2 до 5 лет'),
        (TIER3, 'от 5 до 10 лет'),
        (TIER4, 'от 10 до 15 лет'),
        (TIER5, 'Больше 15 лет'),
    ]

    title = models.CharField(max_length=150)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    salary = models.CharField(max_length=100)
    type = models.CharField(max_length=10,choices=TYPE_CHOICES, default=FULL_TIME)
    experience = models.CharField(max_length=10, choices=EXP_CHOICES, default=TIER1)
    summary = models.TimeField()
    description = models.TimeField()
    logo = models.ImageField(default='default.png',upload_to='upload_images')
    date_created = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return '{} ищет {}'.format(self.company,self.title)