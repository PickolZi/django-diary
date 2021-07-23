from django import forms

from . import models

# Form classes start here.
class EntryForm(forms.ModelForm):

    class Meta():
        model = models.Entry
        fields = "__all__"
    