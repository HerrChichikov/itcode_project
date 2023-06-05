from django.contrib import admin
from core import models

admin.site.register(models.Categories)
admin.site.register(models.Themes)
admin.site.register(models.Person)
admin.site.register(models.Publication)
admin.site.register(models.Profile)
admin.site.register(models.Comment)
