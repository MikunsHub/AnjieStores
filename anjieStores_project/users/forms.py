from django import forms

class NameForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)

class Password(forms.Form):
    password = forms.CharField