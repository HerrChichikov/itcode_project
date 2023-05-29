from django import forms

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
        fields = ['title', 'content', 'theme', 'category', 'person', 'year_start', 'year_end', 'photo', 'is_published', ]


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
        fields = ['name', 'surname', 'patronymic', 'birthday', 'deathday', 'photo', 'bio', ]
