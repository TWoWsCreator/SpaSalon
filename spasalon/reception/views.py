from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages import success
from django.urls import reverse_lazy
from django.views.generic import FormView

from reception.forms import ReceptionForm
from reception.models import Reception
from users.models import CustomUser


class ReceptionView(LoginRequiredMixin, FormView):
    template_name = 'reception/reception.html'
    form_class = ReceptionForm
    model = Reception
    success_url = reverse_lazy('reception:reception')

    def form_valid(self, form):
        user = CustomUser.objects.get(username=self.request.user)
        form.cleaned_data["user"] = user
        self.model.objects.create(**form.cleaned_data)
        success(self.request, 'Ваша заявка принята. Ответ придет на почту.')
        return super().form_valid(form)

