from django.test import TestCase, Client
from django.urls import reverse


class PostsTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_hello(self):
        response = self.client.get(reverse("hello-view"))
        expected_data = "<h1>Страница приветствия</h1>"
        expected_status = 200
        self.assertEqual(response.status_code, expected_status)
        self.assertEqual(response.content.decode(), expected_data)
        self.assertEqual(response["name"], "Alex")

    def test_test_page(self):
        response = self.client.get(reverse("test-page"))
        expected_data = "<h1>Тестовая страница</h1>"
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode(), expected_data)
        # print(response)

    def test_about(self):
        response = self.client.get(reverse("about-page"))
        exp_data = "About"
        self.assertEqual(response.content.decode(), exp_data)
        self.assertEqual(response.status_code, 200)

    def test_contacts(self):
        response = self.client.get(reverse("contacts-page"))
        exp_data = "Contacts"
        self.assertEqual(response.content.decode(), exp_data)
        self.assertEqual(response.status_code, 200)