from django.urls import path

from services.views import (
    ServiceView,
    ServicesView,
)

app_name = "services"
urlpatterns = [
    path("", ServicesView.as_view(), name="services"),
    path("<int:pk>/", ServiceView.as_view(), name="service"),
]
