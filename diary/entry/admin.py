from django.contrib import admin

from . import models

class EntryAdmin(admin.ModelAdmin):
    list_display = ["title", "text", "date"]
    list_filter = ["title", "date"]

    search_fields = ["title"]

# Register your models here.
admin.site.register(models.Entry, EntryAdmin)