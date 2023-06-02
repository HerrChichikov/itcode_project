from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from core import models, datatools, forms, filters
from core.datatools.index import TitleMixin
from django.shortcuts import render

from core.forms import RegisterUserForm, LoginUserForm, UserUpdateForm


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


class RegisterUser(TitleMixin, CreateView):
    title = 'Регистрация'
    form_class = RegisterUserForm
    template_name = 'core/register.html'
    success_url = reverse_lazy('core:main')


class LoginUser(TitleMixin, LoginView):
    title = 'Авторизация'
    form_class = LoginUserForm
    template_name = 'core/login.html'

    def get_success_url(self):
        return reverse_lazy('core:main')

class UserUpdate(TitleMixin, UpdateView):
    title = 'Профиль'
    form_class = UserUpdateForm
    template_name = 'core/user_update.html'
    success_url = reverse_lazy('core:user_update')

    def get_object(self):
        return self.request.user


def logout_user(request):
    logout(request)
    return redirect('core:main')
