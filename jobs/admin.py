from django.contrib import admin
from . import models

admin.site.register(models.Jobs)
admin.site.register(models.Category)
admin.site.register(models.Company)
admin.site.register(models.Applicant)
