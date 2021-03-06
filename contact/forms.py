from django import forms
from contact.models import Contact


class ContactForm(forms.ModelForm):
    fullname = forms.CharField(max_length=10)
    email = forms.EmailField(max_length=50)
    text = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Contact
        fields = ('fullname', 'email', 'text')
