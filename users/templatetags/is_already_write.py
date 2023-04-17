from django import template
from django.contrib.auth.models import User


register = template.Library()

from chat.models import Thread



@register.simple_tag(name='is_already_write')
def is_already_write(first_user, second_user):
    user_1 = User.objects.get(id=first_user)
    user_2 = User.objects.get(id=second_user)
    chat = Thread.objects.filter(first_person=user_1, second_person=user_2)
    if not chat:
        chat = Thread.objects.filter(first_person=user_2, second_person=user_1)

    if chat:
        return True
    else:
        return False