from django.forms import Textarea

from core.forms import BootstrapControlForm
from feedback.models import Feedback


class FeedbackForm(BootstrapControlForm):
    class Meta:
        model = Feedback
        exclude = ('created_on', 'user')
        widgets = {
            'feedback_text': Textarea(attrs={'rows': 5}),
        }
