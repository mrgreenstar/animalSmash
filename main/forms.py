from django import forms

class ChooseForm(forms.Form):
    choose = forms.TextInput(attrs={'type':'image', 'src':'main/pictures/cat.jpg'})
    it = forms.CharField(max_length=100)
