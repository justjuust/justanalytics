from django import forms

class ContactForm(forms.Form):
    email = forms.EmailField(label='Email Address', max_length=254, widget=forms.TextInput(attrs={"class": "form-control"}))
    message = forms.CharField(label='Message', widget=forms.Textarea(attrs={"class": "form-control"}), max_length=2000)