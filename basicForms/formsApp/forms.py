from django import forms
from django.core import validators

# def check_for_a(val):
#     if val[0].lower() != 'a':
#         raise forms.ValidationError('Name needs to start with (a)')


class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    confirm_email = forms.EmailField(label="Please confirm your email:")
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        all_clean_data =super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['confirm_email']

        if email != vmail:
            raise forms.ValidationError("Make Sure Emails Match!!!")

