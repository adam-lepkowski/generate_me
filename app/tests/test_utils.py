from django.test import TestCase
from parameterized import parameterized

from app.utils import generate_nickname, is_leap


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
