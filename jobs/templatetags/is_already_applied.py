from django import template

from ..models import Applicant

register = template.Library()

from django.apps import apps
ChatRoom = apps.get_model('chat', 'ChatRoom')


@register.simple_tag(name='is_already_applied')
def is_already_applied(job, user):
    applied = Applicant.objects.filter(job=job, user=user)
    if applied:
        return True
    else:
        return False

@register.simple_tag(name='is_already_write')
def is_already_applied(job, user):
    name = '{}+{}'.format(job,user)
    chat = ChatRoom.objects.filter(name=name)
    if chat:
        return True
    else:
        return False