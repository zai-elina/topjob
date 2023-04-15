from django.db import models
from django.contrib.auth.models import User

class Interview(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    complete = models.BooleanField(default=False)
    task_date = models.DateTimeField(null=True,blank=True)
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering =['complete']
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
