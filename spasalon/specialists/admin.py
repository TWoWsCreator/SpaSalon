from django.contrib import admin

from specialists.models import Specialists

@ admin.register(Specialists)
class SpecialistsAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'description', 'image_tmb')
