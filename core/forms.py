from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User

from core import models


class PublicationForm(forms.ModelForm):

    # постараться сократить эти проверки и соблюсти DRY
    def clean_title(self):
        title = self.cleaned_data['title']
        if title.isdigit():
            raise forms.ValidationError('Название публикации не должно состоять только из чисел')
        return title

    def clean_content(self):
        content = self.cleaned_data['content']
        if content.isdigit():
            raise forms.ValidationError('Содержание публикации некорректно')
        return content

    class Meta:
        model = models.Publication
        fields = ('title', 'content', 'theme', 'category', 'person', 'year_start', 'year_end', 'photo',
                  'is_published',)
        # fields = "__all__"


class PersonForm(forms.ModelForm):

    # постараться сократить эти проверки и соблюсти DRY
    def clean_name(self):
        name = self.cleaned_data['name']
        if name.isdigit():
            raise forms.ValidationError('Некорректное имя')
        return name

    def clean_surname(self):
        surname = self.cleaned_data['surname']
        if surname.isdigit():
            raise forms.ValidationError('Некорректная фамилия')
        return surname

    def clean_patronymic(self):
        patronymic = self.cleaned_data['patronymic']
        if patronymic.isdigit():
            raise forms.ValidationError('Некорректное отчество')
        return patronymic

    def clean_bio(self):
        bio = self.cleaned_data['bio']
        if bio.isnumeric():
            raise forms.ValidationError('Некорректная биография')
        return bio

    class Meta:
        model = models.Person
        fields = ('name', 'surname', 'patronymic', 'birthday', 'deathday', 'photo', 'bio',)


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserUpdateForm(UserChangeForm):
    email = forms.EmailField(label='Почта', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.TextInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('email', 'password',)


class UserUpdateProfileForm(UserChangeForm):
    nickname = forms.CharField(label='Никнейм', widget=forms.TextInput(attrs={'class': 'form-input'}))
    status = forms.CharField(label='Статус', widget=forms.TextInput(attrs={'class': 'form-input'}))

    class Meta:
        model = models.Profile
        fields = ('nickname', 'profile_photo', 'status',)


class UserCreateProfileForm(forms.ModelForm):
    nickname = forms.CharField(label='Никнейм', widget=forms.TextInput(attrs={'class': 'form-input'}))
    status = forms.CharField(label='Статус', widget=forms.TextInput(attrs={'class': 'form-input'}))

    class Meta:
        model = models.Profile
        fields = ('nickname', 'profile_photo', 'status',)


class PublicationCreatComment(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ('body', 'image', 'parent', )
        # fields = "__all__"


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
