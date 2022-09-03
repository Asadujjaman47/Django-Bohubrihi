from msilib.schema import RadioButton
from xmlrpc.client import boolean
from django import forms


class user_form(forms.Form):
    # boolean_field = forms.BooleanField(required=False)
    # field = forms.CharField(max_length=15, min_length=5)
    # field = forms.ChoiceField(choices=(('', '--SELECT OPTION--'), ('1', 'Firest'), ('2', 'Second'), ('3', 'Third')))

    # tuple 1st value: database value,
    #       2nd value: webpage show value
    # choices = (('A', 'A'), ('B', 'B'), ('C', 'C'))
    # field = forms.ChoiceField(choices=choices, widget=forms.RadioSelect)

    # choices = (('', '--SELECT OPTION--'), ('1', 'Firest'),
    #            ('2', 'Second'), ('3', 'Third'))
    # field = forms.MultipleChoiceField(
    #     choices=choices, required=False)

    choices = (('A', 'A'), ('B', 'B'), ('C', 'C'))
    field = forms.MultipleChoiceField(
        choices=choices)
