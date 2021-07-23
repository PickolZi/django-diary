from django.contrib import admin

from . import models

class EntryAdmin(admin.ModelAdmin):
    list_display = ["title", "text"]
    list_filter = ["title"]

    search_fields = ["title"]

# Register your models here.
admin.site.register(models.Entry, EntryAdmin)