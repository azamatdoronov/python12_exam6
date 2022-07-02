from django import forms
from django.forms import widgets


class GuestbookForm(forms.Form):
    author = forms.CharField(max_length=20, required=True, label='Автор:')
    email = forms.EmailField(max_length=20, empty_value=True, required=True, label='Email:')
    note = forms.CharField(max_length=2000, required=True, widget=widgets.Textarea(attrs={"cols": 40, "rows": 3}),
                           label="Текст:")
