# import factory
# from faker import Factory
#
# from core import models
#
# factory_ru = Factory.create('ru-Ru')
#
#
# class User(factory.django.DjangoModelFactory):
#     name = factory_ru.word()
#
#     class Meta:
#         model = models.User
#
#
# class School(factory.django.DjangoModelFactory):
#     name = factory_ru.word()
#
#     class Meta:
#         model = models.School
#
#
# class Course(factory.django.DjangoModelFactory):
#     # name = factory_ru.word()
#     name = factory.Sequence(lambda n: "Course #%s" % n)
#
#     class Meta:
#         model = models.Course
#
#
# class Account(factory.django.DjangoModelFactory):
#     user = factory.SubFactory(User)
#     login = factory_ru.word()
#     password = factory_ru.password()
#     school = factory.SubFactory(School)
#
#     class Meta:
#         model = models.Account
#
#     @factory.post_generation
#     def course(self, create, extracted, **kwargs):
#         if not create:
#             # Simple build, do nothing.
#             return
#
#         if extracted:
#             # A list of groups were passed in, use them
#             # for cour in extracted:
#             self.course.add(extracted)
