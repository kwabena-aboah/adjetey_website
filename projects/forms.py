from django import forms
from . models import Contact


class ContactForm(forms.ModelForm):
    # name = forms.CharField(
    #     label = 'Name',
    #     widget = forms.CharField(
    #         attrs = {'class': 'form-control', 'placeholder': 'Name'}
    #     )
    # )
    # email = forms.EmailField(
    #     label = 'Email',
    #     widget = forms.EmailField(
    #         attrs = {'class': 'form-control', 'placeholder': 'Email'}
    #     )
    # )
    # message = forms.CharField(
    #         label = 'Message',
    #         widget = forms.TextInput(
    #             attrs = {'class': 'form-control', 'cols': 30, 'rows': 7, 'placeholder': 'Message'}
    #         )
    #     )

    class Meta:
        model = Contact
        fields = (
            'name', 'email', 'message',
        )
        labels = {'name': ''}
