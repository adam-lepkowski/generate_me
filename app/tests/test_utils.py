from unittest.mock import patch

from django.test import TestCase
from parameterized import parameterized

from app.models import LastNameModel, FirstNameModel
from app.utils import generate_nickname, is_leap, draw_dob, draw_identity


class TestGenerateNickname(TestCase):

    @parameterized.expand([
        ("no_special_char", "foo", "bar"),
        ("hyphen_fname", "-foo-", "bar"),
        ("hyphen_lname", "foo", "b-ar-"),
        ("space_fname", " foo ", "bar"),
        ("space_lname", "foo", " bar  ")
    ])
    def test_generate_nickname(self, name, fname, lname):
        result = generate_nickname(fname, lname)
        self.assertTrue(result.startswith("f"))
        self.assertTrue("-" not in result)
        self.assertTrue(" " not in result)


class TestIsLeap(TestCase):

    @parameterized.expand([
        ("dividable_400_100", 400, True, "assertTrue"),
        ("dividable_4_not_100", 2020, True, "assertTrue"),
        ("not_400_100_4", 2017, False, "assertFalse")

    ])
    def test_is_leap(self, name, year, expected, func):
        getattr(self, func)(expected, is_leap(year))


class TestDrawDob(TestCase):

    @patch("app.utils.random.randint", side_effect=[2020, 2, 28])
    def test_draw_dob(self, mock_randint):
        result = draw_dob()
        expected = "2020-02-28"
        self.assertEqual(expected, result)
        self.assertTrue(mock_randint.call_count == 3)


class TestDrawIdentity(TestCase):

    def setUp(self):
        FirstNameModel.objects.create(first_name="Foo", gender="male")
        LastNameModel.objects.create(last_name="Bar", gender="male")

    @patch("app.utils.generate_nickname", return_value="foo.bar")
    @patch("app.utils.draw_dob", return_value="2020-10-10")
    def test_draw_identity(self, mock_dob, mock_nickname):
        expected = {
            "first_name": "Foo",
            "last_name": "Bar",
            "gender": "male",
            "dob": "2020-10-10",
            "nickname": "foo.bar"
        }
        result = draw_identity()
        self.assertEqual(expected, result)
