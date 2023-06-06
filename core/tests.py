import datetime

from django.test import TestCase, Client
from django.urls import reverse
from core import factories, models


class PublicationTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.user = models.User.objects.create(username='testuser', password='testuser', email='test@mail.ru', )
        self.categories = factories.Categories()
        self.themes = factories.Themes()
        self.profile = factories.Profile(user = self.user)
        self.person = factories.Person(author = self.profile)
        self.publication = factories.Publication(theme = self.themes, category = self.categories, author =self.profile, )
        self.comment = factories.Comment(publication = self.publication, profile = self.profile)

    def test_publications_list(self):
        response = self.client.get(reverse('core:publications'))
        self.assertEqual(response.status_code, 200)

    def test_publications_detail(self):
        response = self.client.get(reverse('core:publication_detail', kwargs={'pk': self.publication.pk}, ))
        self.assertEqual(response.status_code, 200)

    def test_publications_create(self):
        data = {
            'title': 'test_title',
            'content': 'test_con',
            'theme': 'test_theme',
            'category': self.categories,
            'person': self.profile,
            'year_start': datetime.date,
            'year_end': datetime.date,
            'author': self.profile,
        }
        response = self.client.post(path=reverse('core:publication_create'), data=data, follow=True, )
        self.assertEqual(response.status_code, 200)
