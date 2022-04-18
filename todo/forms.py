""" form system """
from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
    """ Form class """
    class Meta:
        """ form """
        model = Item
        fields = ['name', 'done']
