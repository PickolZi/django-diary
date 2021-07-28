from django import forms

from . import models

# Form classes start here.
class EntryForm(forms.ModelForm):

    class Meta():
        model = models.Entry
        fields = ("title", "text")

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
        }
    