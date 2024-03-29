from unittest.mock import patch

from django.test import TestCase

from app.views import IndexView


class TestIndex(TestCase):

    def test_index_get(self):
        response = self.client.get("/")
        self.assertEqual(200, response.status_code)

    def test_index_view_get(self):
        response = self.client.get("/")
        self.assertEqual(response.resolver_match.func.view_class, IndexView)

    def test_index_post_disallowed(self):
        response = self.client.post("/")
        self.assertEqual(405, response.status_code)

