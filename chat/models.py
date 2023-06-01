from django.contrib.auth.models import User
from django.db import models
from django.db.models import Q


class ThreadManager(models.Manager):
    def by_user(self, **kwargs):
        user = kwargs.get('user')
        lookup = Q(first_person=user) | Q(second_person=user)
        qs = self.get_queryset().filter(lookup).distinct()
        return qs


class Thread(models.Model):
    first_person = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True,related_name='thread_first_person')
    second_person = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,
                                     related_name='thread_second_person')
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = ThreadManager()

    class Meta:

        unique_together = ['first_person', 'second_person']
        verbose_name = "Диалог"
        verbose_name_plural = "Диалоги"


class ChatMessage(models.Model):
    thread = models.ForeignKey(Thread, null=True, blank=True, on_delete=models.CASCADE, related_name='chatmessage_thread')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message_text = models.TextField(blank=True)
    message_file = models.FileField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def save_message(self, message_text=None, message_file=None):
        if message_text:
            self.message_text = message_text
        if message_file:
            self.message_file = message_file
        self.save()

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"