from django.forms import SelectDateWidget

from core.forms import BootstrapControlForm
from reception.models import Reception

class ReceptionForm(BootstrapControlForm):
    class Meta:
        model = Reception
        exclude = ('user',)
        widgets = {
            'reception_date': SelectDateWidget(),
        }