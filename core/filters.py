import django_filters as filters
from django import forms

from core import models


class PublicationSearch(filters.FilterSet):
    class Meta:
        model = models.Publication
        fields = ('title', 'person', 'theme', 'category', )


class PersonSearch(filters.FilterSet):
    class Meta:
        model = models.Person
        fields = ('name', 'surname', 'patronymic', )


class ProfileSearch(filters.FilterSet):
    class Meta:
        model = models.Profile
        fields = ('nickname', )
