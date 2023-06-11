from django.views.generic import DetailView, ListView
from django.db import models

from services.models import Services, ServiceImages

class ServicesView(ListView):
    template_name = "services/services.html"
    context_object_name = "services"

    def get_queryset(self):
        return Services.objects.filter(is_published=True)
    

class ServiceView(DetailView):
    template_name = "services/service.html"
    context_object_name = "service"
    model = Services
    queryset = model.objects.all()

    def get_object(self):
        service_images = ServiceImages.objects.only(
            'service_photos', 'image'
        )
        service_images_field = ServiceImages.service_photos
        return self.queryset.prefetch_related(
                models.Prefetch(
                service_images_field.field.related_query_name(),
                queryset=service_images,
            )).filter(is_published=True).get(pk=self.kwargs["pk"])