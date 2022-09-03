from dataclasses import field, fields
from django import forms
# from first_app.models import Album, Musician
from first_app import models


class MusicianForm(forms.ModelForm):
    class Meta:
        model = models.Musician

        # model all field include korbe
        fields = "__all__"

        # if exclude: kono field baad dite chaile
        # exclude = ['first_name']

        # new field add korte chaile
        # fields = ('first_name', 'last_name',)
