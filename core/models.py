
from django.contrib.auth.models import User
from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Categories(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название категории', )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категории публикаций"


class Themes(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название темы', )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Темы публикаций"


class Person(models.Model):
    surname = models.CharField(max_length=255, verbose_name='Фамилия', )
    name = models.CharField(max_length=255, verbose_name='Имя', )
    patronymic = models.CharField(max_length=255, verbose_name='Отчество', blank=True, )
    birthday = models.DateField(verbose_name='Дата рождения', null=True, )
    deathday = models.DateField(verbose_name='Дата смерти', blank=True, null=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фотография личности', blank=True, )
    bio = models.TextField(verbose_name='Текст биографии', blank=True, )
    time_publish = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации', null=True, )
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата обновления', null=True, )
    author = models.ForeignKey("Profile", on_delete=models.CASCADE, verbose_name='Автор личности',
                               related_name='person_profiles', null=True)
    def __str__(self):
        return f'{self.name} {self.patronymic} {self.surname}'

    class Meta:
        ordering = ["surname"]
        verbose_name = "Историческая личность"

    # def get_absolute_url(self):
    #     return reverse('#', kwargs = {})


class Publication(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название публикации')
    content = models.TextField(verbose_name='Текст публикации', )
    theme = models.ForeignKey(Themes, on_delete=models.PROTECT, verbose_name='Тема публикации',
                              related_name='publications', )
    category = models.ForeignKey(Categories, on_delete=models.PROTECT, verbose_name='Категория публикации',
                                 related_name='categories', )
    person = models.ManyToManyField(Person, verbose_name='Связанные личности',
                                    related_name='persons', blank=True, )
    year_start = models.DateField(verbose_name='Дата начала события или первого появления вещи', )
    year_end = models.DateField(verbose_name='Дата окончания события', )
    time_publish = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации', )
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата обновления', )
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото события или вещи', blank=True, )
    author = models.ForeignKey("Profile", on_delete=models.CASCADE, verbose_name='Автор публикации',
                               related_name='publication_profiles', null=True)
    likes = models.ManyToManyField(User, verbose_name='Лайки публикации',
                                  related_name='publication_likes', blank=True, )
    is_published = models.BooleanField(default=True, )

    def __str__(self):
        return f"{self.title}"

    def number_of_likes(self):
        return self.likes.count()

    class Meta:
        ordering = ["-time_publish"]
        verbose_name = "Публикация"
    # def get_absolute_url(self):
    #     return reverse('#', kwargs = {})


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, verbose_name='Пользователь', )
    nickname = models.CharField(max_length=255, verbose_name='Никнейм профиля', blank=True, )
    status = models.TextField(verbose_name='Статус профиля', blank=True, )
    profile_photo = models.ImageField(upload_to='photos/profile_pic/%Y/%m/%d/', verbose_name='Фото профиля', blank=True,
                                      null=True, )

    def __str__(self):
        return f"{self.nickname}"

    class Meta:
        verbose_name = "Профиль"
    # def get_absolute_url(self):
    #     return reverse('#', kwargs = {})


class Comment(MPTTModel):
    publication = models.ForeignKey(Publication, related_name="comment_publications", on_delete=models.CASCADE,
                                    verbose_name="Публикация комментария", )
    profile = models.ForeignKey(Profile, related_name="comment_profile", on_delete=models.CASCADE,
                                verbose_name="Комментатор", )
    body = models.TextField(verbose_name='Тело комментария', )
    image = models.ImageField(upload_to='photos/comments/%Y/%m/%d/', verbose_name='Фото комментария', blank=True, )
    date = models.DateTimeField(auto_now_add=True, verbose_name='Время и дата комментария')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children', verbose_name="parent comment", )

    class MPTTMeta:
        level_attr = "Ответ комментарию #"
        order_insertion_by = ['body']

    def __str__(self):
        return f"{self.profile.nickname} #{self.id}"

    class Meta:
        ordering = ["date"]
        verbose_name = "Комментарий"