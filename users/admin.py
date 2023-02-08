from django.contrib import admin
from .models import Resume, Experience,Education

admin.site.register(Experience)
admin.site.register(Resume)
admin.site.register(Education)