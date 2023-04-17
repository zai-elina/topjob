from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from jobs.models import Company
from django.template.defaultfilters import slugify
from uuid import uuid4


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    company = models.ForeignKey(Company,on_delete =models.CASCADE, null=True,blank=True)
    date = models.DateField(default=timezone.now)
    image = models.ImageField(default='post.jpg', upload_to='company-blog')
    slug = models.SlugField(null=True, blank=True, unique=True, max_length=500)
    uniqueId = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'{self.title}, {self.company}'

    def save(self,*args,**kwargs):
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[0]
            self.slug = slugify('post-{}-{}'.format(self.title,self.uniqueId))

        self.slug=slugify('post-{}-{}'.format(self.title,self.uniqueId))

        super(Post,self).save(*args,**kwargs)


    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'


class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text_comments = models.TextField('Текст комментария', max_length=2000)
    post = models.ForeignKey(Post, verbose_name='Публикация', on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return f'{self.user.username}, {self.post}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

