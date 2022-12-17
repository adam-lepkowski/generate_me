from unittest.mock import patch

from django.test import TestCase

from app.views import IndexView


IDENTITY = {
    "first_name": "foo",
    "last_name": "bar",
    "gender": "male",
    "dob": "2020-10-10",
    "nickname": "foo.bar"
}


class TestIndex(TestCase):

    def test_index_get(self):
        response = self.client.get("/")
        self.assertEqual(200, response.status_code)

    def test_index_view_get(self):
        response = self.client.get("/")
        self.assertEqual(response.resolver_match.func.view_class, IndexView)

    @patch("app.views.draw_identity", return_value=IDENTITY)
    def test_index_post(self, indentity_mock):
        response = self.client.post("/")
        self.assertEqual(200, response.status_code)

    @patch("app.views.GeneratorForm")
    @patch("app.views.draw_identity", return_value=IDENTITY)
    def test_index_post_context(self, indentity_mock, gen_form_mock):
        response = self.client.post("/")
        result = {
            "form": response.context["form"],
            "gender": response.context["gender"],
        }
        expected = {
            "form": gen_form_mock(),
            "gender": IDENTITY["gender"]
        }
        self.assertEqual(expected, result)
