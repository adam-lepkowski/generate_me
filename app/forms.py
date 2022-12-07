from django import forms


class GeneratorForm(forms.Form):
    gender = forms.CharField(max_length=6)
    first_name = forms.CharField(max_length=75)
    last_name = forms.CharField(max_length=75)
    dob = forms.DateField(label="Date of birth")
    nickname = forms.CharField(max_length=155)