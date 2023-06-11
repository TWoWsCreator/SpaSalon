from django.views.generic import DetailView, ListView

from specialists.models import Specialists

class SpecialistsView(ListView):
    template_name = "specialists/specialists.html"
    context_object_name = "specialists"

    def get_queryset(self):
        return Specialists.objects.filter(is_published=True)
    

class SpecialistView(DetailView):
    template_name = "specialists/specialist.html"
    context_object_name = "specialist"
    model = Specialists
    queryset = model.objects.all()

    def get_object(self):
        return self.queryset.filter(is_published=True).get(pk=self.kwargs["pk"])