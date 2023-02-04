from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

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

    title = models.CharField(max_length=150)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    salary = models.CharField(max_length=100)
    type = models.CharField(max_length=50,choices=TYPE_CHOICES, default=FULL_TIME)
    experience = models.CharField(max_length=50, choices=EXP_CHOICES, default=TIER1)
    summary = models.TextField()
    description = models.TextField()
    logo = models.ImageField(upload_to='company_logo', blank=True)
    date_created = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return '{} ищет {}'.format(self.company,self.title)

    class Meta:
        verbose_name ="Вакансия"
        verbose_name_plural = "Вакансии"




