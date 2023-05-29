import django_filters as filters
from core import models


class PublicationSearch(filters.FilterSet):
    class Meta:
        model = models.Publication
        fields = ['title', 'person', ]


class PersonSearch(filters.FilterSet):
    class Meta:
        model = models.Person
        fields = ['name', 'surname', 'patronymic', ]
