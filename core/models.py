from django.db import models

CATEGORIES = (

    ('Статья', 'Статья'),
    ('Факт', 'Факт'),
    ('Юмор', 'Юмор'),

)

THEMES = (

    ('Событие', 'Событие'),
    ('Вещь', 'Вещь'),

)


class Categories(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название категории', )

    def __str__(self):
        return self.name


class Themes(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название темы', )

    def __str__(self):
        return self.name


class Person(models.Model):
    surname = models.CharField(max_length=255, verbose_name='Фамилия', )
    name = models.CharField(max_length=255, verbose_name='Имя', )
    patronymic = models.CharField(max_length=255, verbose_name='Отчество', blank=True, )
    birthday = models.DateField(verbose_name='Дата рождения', null=True, )
    deathday = models.DateField(verbose_name='Дата смерти', blank=True, null=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фотография личности', blank=True, )
    bio = models.TextField(verbose_name='Текст публикации', blank=True, )
    time_publish = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации', null=True, )
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата обновления', null=True, )

    def __str__(self):
        return f'{self.name} {self.patronymic} {self.surname}'

    # def get_absolute_url(self):
    #     return reverse('#', kwargs = {})


class Publication(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название публикации')
    content = models.TextField(verbose_name='Текст публикации', )
    theme = models.ForeignKey(Themes, on_delete=models.PROTECT, verbose_name='Тема публикации',
                              related_name='Publication', )
    category = models.ForeignKey(Categories, on_delete=models.PROTECT, verbose_name='Категория публикации',
                                 related_name='Publication', )
    person = models.ManyToManyField(Person, verbose_name='Связанные личности',
                                    related_name='Publication', )
    year_start = models.DateField(verbose_name='Дата начала события или первого появления вещи', )
    year_end = models.DateField(verbose_name='Дата окончания события', )
    time_publish = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации', )
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата обновления', )
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото события или вещи', blank=True, )
    is_published = models.BooleanField(default=True, )

    def __str__(self):
        return f"{self.title}"

    # def get_absolute_url(self):
    #     return reverse('#', kwargs = {})
