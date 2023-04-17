from django import template
from django.contrib.auth.models import User

from ..models import Applicant

register = template.Library()

from users.models import Favorite


@register.simple_tag(name='is_already_applied')
def is_already_applied(job, user):
    applied = Applicant.objects.filter(job=job, user=user)
    if applied:
        return True
    else:
        return False


@register.simple_tag(name='is_already_liked')
def is_already_liked(job, user):
    liked = Favorite.objects.filter(job=job, user=user)
    if liked:
        return True
    else:
        return False


