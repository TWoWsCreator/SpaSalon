from django.urls import path

from specialists.views import (
    SpecialistView,
    SpecialistsView,
)

app_name = "specialists"
urlpatterns = [
    path("", SpecialistsView.as_view(), name="specialists"),
    path("<int:pk>/", SpecialistView.as_view(), name="specialist"),
]