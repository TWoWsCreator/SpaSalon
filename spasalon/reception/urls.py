from django.urls import path

from reception.views import ReceptionView

app_name = 'reception'
urlpatterns = [
    path('', ReceptionView.as_view(), name='reception')
]
