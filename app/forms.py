from django import forms


class GeneratorForm(forms.Form):
    first_name = forms.CharField(max_length=75, required=False)
    last_name = forms.CharField(max_length=75, required=False)
    dob = forms.DateField(label="Date of birth", required=False)
    nickname = forms.CharField(max_length=155, required=False)