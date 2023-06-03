from django.contrib import admin
from core.models import Categories, Themes, Person, Publication, Profile

admin.site.register(Categories)
admin.site.register(Themes)
admin.site.register(Person)
admin.site.register(Publication)
admin.site.register(Profile)

