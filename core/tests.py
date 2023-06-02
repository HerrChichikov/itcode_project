# from django.test import TestCase, Client
# from django.urls import reverse
# from core import factories
#
#
# class AccountTest(TestCase):
#     def setUp(self) -> None:
#         self.client = Client()
#         self.user = factories.User()
#         self.school = factories.School()
#         self.course = factories.Course.create(name='course')
#         self.account = factories.Account(user=self.user, school=self.school, course=self.course)
#
#     def test_accounts_data(self):
#         response = self.client.get(reverse('core:accounts'))
#         self.assertEqual(response.status_code, 200)
#
#     def test_account_detail(self):
#         response = self.client.get(reverse('core:account_detail', kwargs={'pk': self.account.pk}, ))
#         self.assertEqual(response.status_code, 200)
#
#     def test_account_create(self):
#         data = {
#             'user': self.user,
#             'login': 'test_log',
#             'password': 'test_pas',
#             'course': self.course,
#             'school': self.school,
#         }
#         response = self.client.post(path=reverse('core:account_create'), data=data, follow=True, )
#         self.assertEqual(response.status_code, 200)
