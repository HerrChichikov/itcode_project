import factory
from faker import Factory

from core import models

factory_ru = Factory.create('ru-Ru')


class Categories(factory.django.DjangoModelFactory):
    name = factory_ru.word()

    class Meta:
        model = models.Categories


class Themes(factory.django.DjangoModelFactory):
    name = factory_ru.word()

    class Meta:
        model = models.Themes


class User(factory.django.DjangoModelFactory):
    username = factory_ru.word()
    password = factory_ru.password()
    email = factory_ru.email()

    class Meta:
        model = models.User


class Profile(factory.django.DjangoModelFactory):
    user = factory.SubFactory(User)
    nickname = factory_ru.user_name()
    status = factory_ru.word()
    profile_photo = factory_ru.image_url()

    class Meta:
        model = models.Profile


class Person(factory.django.DjangoModelFactory):
    surname = factory_ru.word()
    name = factory_ru.word()
    patronymic = factory_ru.word()
    birthday = factory_ru.date()
    deathday = factory_ru.date()
    bio = factory_ru.word()
    time_publish = factory_ru.date()
    time_update = factory_ru.date()
    author = factory.SubFactory(Profile)

    class Meta:
        model = models.Person


class Publication(factory.django.DjangoModelFactory):
    title = factory_ru.word()
    content = factory_ru.word()
    theme = factory.SubFactory(Themes)
    category = factory.SubFactory(Categories)
    year_start = factory_ru.date()
    year_end = factory_ru.date()
    time_publish = factory_ru.date()
    time_update = factory_ru.date()
    author = factory.SubFactory(Profile)
    is_published = factory_ru.boolean()

    class Meta:
        model = models.Publication

    @factory.post_generation
    def person(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            self.person.add(extracted)


class Comment(factory.django.DjangoModelFactory):
    publication = factory.SubFactory(Publication)
    profile = factory.SubFactory(Profile)
    body = factory_ru.word()
    date = factory_ru.date()

    class Meta:
        model = models.Comment