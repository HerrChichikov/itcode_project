from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from core import models, datatools, forms, filters
from core.datatools.index import TitleMixin
from django.shortcuts import render


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

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        likes_connected = get_object_or_404(models.Publication, id=self.kwargs['pk'])
        liked = False
        if likes_connected.likes.filter(id=self.request.user.id).exists():
            liked = True
        data['number_of_likes'] = likes_connected.number_of_likes()
        data['post_is_liked'] = liked
        return data


def publication_like(request, pk):
    post = get_object_or_404(models.Publication, id=request.POST.get('publication_id'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return HttpResponseRedirect(reverse('core:publication_detail', args=[str(pk)]))


class PublicationCreate(TitleMixin, CreateView):
    model = models.Publication
    template_name = 'core/publication_create.html'
    form_class = forms.PublicationForm
    title = 'Создание публикации'
    success_url = reverse_lazy('core:publications')

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        return super().form_valid(form)


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


class PublicationCommentCreate(TitleMixin, CreateView):
    template_name = 'core/publication_comment_create.html'
    form_class = forms.PublicationCreatComment
    title = 'Комментарий'
    success_url = reverse_lazy('core:publications')

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        form.instance.publication_id = self.kwargs['pk']
        return super().form_valid(form)


class PublicationCommentDelete(TitleMixin, DeleteView):
    model = models.Comment
    template_name = 'core/publication_comment_delete.html'
    fields = "__all__"
    title = 'Удаление комментария'
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

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        return super().form_valid(form)


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
    form_class = forms.RegisterUserForm
    template_name = 'core/register.html'
    success_url = reverse_lazy('core:main')


class LoginUser(TitleMixin, LoginView):
    title = 'Авторизация'
    form_class = forms.LoginUserForm
    template_name = 'core/login.html'

    def get_success_url(self):
        return reverse_lazy('core:main')


class UserUpdate(TitleMixin, UpdateView):
    title = 'Настройки'
    form_class = forms.UserUpdateForm
    template_name = 'core/user_update.html'
    success_url = reverse_lazy('core:user_update')

    def get_object(self):
        return self.request.user


class ProfileDetail(TitleMixin, DetailView):
    model = models.Profile
    template_name = 'core/user_profile.html'
    context_object_name = 'profile'
    title = 'Профиль'


class ProfileUpdate(TitleMixin, UpdateView):
    model = models.Profile
    title = 'Изменение профиля'
    form_class = forms.UserUpdateProfileForm
    template_name = 'core/user_profile_update.html'
    success_url = reverse_lazy('core:user_profile_update')

    def get_object(self):
        return self.request.user.profile


class ProfileCreate(TitleMixin, CreateView):
    models = models.Profile
    title = 'Создание профиля'
    form_class = forms.UserCreateProfileForm
    template_name = 'core/user_profile_create.html'
    success_url = reverse_lazy('core:user_profile_update')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProfileList(TitleMixin, ListView):
    model = models.Profile
    template_name = 'core/user_profile_list.html'
    context_object_name = 'profiles'
    title = 'Профили'

    def get_filters(self):
        return filters.ProfileSearch(self.request.GET)

    def get_queryset(self):
        return self.get_filters().qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.get_filters()
        return context


class ProfileDelete(TitleMixin, DeleteView):
    model = models.Profile
    template_name = 'core/user_profile_delete.html'
    fields = "__all__"
    title = 'Удаление профиля'
    success_url = reverse_lazy('core:profiles')


class ProfileChangeRole(TitleMixin, UpdateView):
    model = models.User
    template_name = 'core/user_profile_change_role.html'
    fields = ('is_staff', 'is_superuser',)
    title = 'Смена прав'
    success_url = reverse_lazy('core:profiles')


def logout_user(request):
    logout(request)
    return redirect('core:main')
