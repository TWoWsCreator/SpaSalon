from django.contrib import admin

from reception.models import Reception

@ admin.register(Reception)
class ReceptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'mail', 'service', 'specialist', 'reception_date')