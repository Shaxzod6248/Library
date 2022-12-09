from django import forms
from .models import BookSearch


class BookSearchForm(forms.ModelForm):
    name_of_book = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': "form-control me-2", 'placeholder': 'Kitob nomini kiriting'
    }))
    class Meta:
        model = BookSearch
        fields = ['name_of_book',]