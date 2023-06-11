from django.contrib.auth.decorators import login_required
from django.urls import path

from reviews.views import (
    AddReviewView,
    ReviewsView,
)

app_name = "reviews"
urlpatterns = [
    path("", ReviewsView.as_view(), name="reviews"),
    path("add_review/", login_required(AddReviewView.as_view()), name="add_review"),
]
