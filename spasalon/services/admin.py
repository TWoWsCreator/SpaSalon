from django.contrib import admin

from services.models import Services, ServiceImages

class ServiceImagesAdmin(admin.TabularInline):
    model = ServiceImages

@ admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'image_tmb')
    inlines = (ServiceImagesAdmin,)