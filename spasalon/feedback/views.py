from django.contrib.messages import success
from django.urls import reverse_lazy
from django.views.generic import FormView

from feedback.forms import FeedbackForm
from feedback.models import Feedback
from users.models import CustomUser


class FeedbackView(FormView):
    template_name = 'feedback/feedback.html'
    form_class = FeedbackForm
    model = Feedback
    success_url = reverse_lazy('feedback:feedback')

    def form_valid(self, form):
        # print(self.request.user, self.request.user == 'AnonymousUser')
        if self.request.user.is_authenticated:
            user = CustomUser.objects.get(username=self.request.user)
            form.cleaned_data["user"] = user
        self.model.objects.create(**form.cleaned_data)
        success(self.request, 'Ваше отзыв отправлен успешно')
        return super().form_valid(form)

