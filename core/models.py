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


class Person(models.Model):
    surname = models.CharField(max_length=255, verbose_name='Фамилия', )
    name = models.CharField(max_length=255, verbose_name='Имя', )
    patronymic = models.CharField(max_length=255, verbose_name='Отчество', blank=True, )
    birthday = models.DateField(verbose_name='Дата рождения', null=True, )
    deathday = models.DateField(verbose_name='Дата смерти', blank=True, null=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фотография личности')
    bio = models.TextField(verbose_name='Текст публикации', blank=True, )

    def __str__(self):
        return f'{self.name} {self.surname}'


class Publication(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название публикации')
    content = models.TextField(verbose_name='Текст публикации', )
    theme = models.CharField(max_length=255, choices=CATEGORIES, default=THEMES[0],
                             verbose_name='Тема публикации', )
    category = models.CharField(max_length=255, choices=CATEGORIES, default=CATEGORIES[0],
                                verbose_name='Категория публикации', )
    person = models.ForeignKey(Person, on_delete=models.CASCADE, verbose_name='Связанные личности',
                               related_name='Publication', )
    year_start = models.DateField(verbose_name='Дата начала события или первого появления вещи', )
    year_end = models.DateField(verbose_name='Дата окончания события', )
    time_publish = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации', )
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата обновления', )
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото события или вещи')
    is_published = models.BooleanField(default=True, )

    def __str__(self):
        return f"{self.title}"
