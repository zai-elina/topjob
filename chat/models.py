from django.db import models
from uuid import uuid4
from django.template.defaultfilters import slugify


class  ChatRoom(models.Model):
    uniqueId = models.CharField(null=True, max_length=100, blank=True)
    name = models.CharField(max_length=100,unique=True)
    slug = models.SlugField(unique=True)

    def save(self,*args,**kwargs):
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[0]
            self.slug = slugify('{} {}'.format(self.name, self.uniqueId))


        self.slug = slugify('{} {}'.format(self.name, self.uniqueId))

        super(ChatRoom,self).save(*args,**kwargs)

    class Meta:
        verbose_name = "Чат"
        verbose_name_plural = "Чаты"