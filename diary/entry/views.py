from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.base import TemplateView

from django.urls import reverse_lazy

from . import models
from . import forms

# Create your views here.
class EntryView(ListView):
    model = models.Entry
    template_name = 'entry/entries.html'
    context_object_name = "entries"


class CreateEntryView(CreateView):
    model = models.Entry
    form_class = forms.EntryForm
    template_name = 'entry/entry_form.html'
    # fields = "__all__"


class DeleteEntryView(DeleteView):
    model = models.Entry
    success_url = reverse_lazy("entry:entries")
