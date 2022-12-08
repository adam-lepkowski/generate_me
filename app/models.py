from django.db import models


class FirstNameModel(models.Model):
    """
    First name with assigned gender.
    """

    first_name = models.CharField(max_length=40)
    gender = models.CharField(max_length=6)

    def __str__(self):
        return f"{self.first_name}: {self.gender}"


class LastNameModel(models.Model):
    """
    Last name with assigned gender.
    """

    last_name = models.CharField(max_length=40)
    gender = models.CharField(max_length=6)

    def __str__(self):
        return f"{self.last_name}: {self.gender}"