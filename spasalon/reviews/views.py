from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import FormView, ListView

from reviews.forms import ReviewsForm
from reviews.models import Reviews
from users.models import CustomUser

class AddReviewView(LoginRequiredMixin, FormView):
    template_name = "reviews/add_review.html"
    form_class = ReviewsForm
    model = Reviews
    success_url = reverse_lazy("reviews:reviews")

    def form_valid(self, form):
        user = CustomUser.objects.get(username=self.request.user)
        form.cleaned_data["user"] = user
        self.model.objects.create(**form.cleaned_data)
        return super().form_valid(form)


class ReviewsView(ListView):
    template_name = "reviews/reviews.html"
    context_object_name = "reviews"

    def get_queryset(self):
        return Reviews.objects.filter(is_published=True).order_by('created_on')