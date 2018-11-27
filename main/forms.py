from django import forms

class AddAnimalForm(forms.Form):
    name = forms.CharField(max_length=32)
    