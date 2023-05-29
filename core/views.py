from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from core import models, datatools, forms, filters
from .datatools.index import *
from django.shortcuts import render

menu = [{'title': "О сайте", 'url_name': 'core:about'},
        {'title': "Добавить публикацию", 'url_name': 'core:add_page'},
        {'title': "Войти", 'url_name': 'core:login'},
        ]


class PublicationList(TitleMixin, ListView):
    model = models.Publication
    template_name = 'core/publication_list.html'
    context_object_name = 'publications'
    title = 'Все публикации'

    def get_filters(self):
        return filters.PublicationSearch(self.request.GET)

    def get_queryset(self):
        return self.get_filters().qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.get_filters()
        return context


class PublicationDetail(TitleMixin, DetailView):
    model = models.Publication
    template_name = 'core/publication_detail.html'
    context_object_name = 'publication'
    title = 'Полная публикация'


class PublicationCreate(TitleMixin, CreateView):
    model = models.Publication
    template_name = 'core/publication_create.html'
    form_class = forms.PublicationForm
    title = 'Создание публикации'
    success_url = reverse_lazy('core:publications')


class PublicationUpdate(TitleMixin, UpdateView):
    model = models.Publication
    template_name = 'core/publication_update.html'
    form_class = forms.PublicationForm
    title = 'Обновление публикации'
    success_url = reverse_lazy('core:publications')


class PublicationDelete(TitleMixin, DeleteView):
    model = models.Publication
    template_name = 'core/publication_delete.html'
    fields = "__all__"
    title = 'Удаление публикации'
    success_url = reverse_lazy('core:publications')


class PersonList(TitleMixin, ListView):
    model = models.Person
    template_name = 'core/person_list.html'
    context_object_name = 'persons'
    title = 'Список личностей'

    def get_filters(self):
        return filters.PersonSearch(self.request.GET)

    def get_queryset(self):
        return self.get_filters().qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.get_filters()
        return context


class PersonDetail(TitleMixin, DetailView):
    model = models.Person
    template_name = 'core/person_detail.html'
    context_object_name = 'person'
    title = 'Подробнее о личности'


class PersonCreate(TitleMixin, CreateView):
    model = models.Person
    template_name = 'core/person_create.html'
    form_class = forms.PersonForm
    title = 'Добавление личности'
    success_url = reverse_lazy('core:persons')


class PersonUpdate(TitleMixin, UpdateView):
    model = models.Person
    template_name = 'core/person_update.html'
    form_class = forms.PersonForm
    title = 'Обновление данных о личности'
    success_url = reverse_lazy('core:persons')


class PersonDelete(TitleMixin, DeleteView):
    model = models.Person
    template_name = 'core/person_delete.html'
    fields = "__all__"
    title = 'Удаление личности'
    success_url = reverse_lazy('core:persons')


def get_main_page(request):
    return render(request=request, template_name='core/main.html')
