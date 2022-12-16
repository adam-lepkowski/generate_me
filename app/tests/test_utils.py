from django.test import TestCase
from parameterized import parameterized

from app.utils import generate_nickname


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