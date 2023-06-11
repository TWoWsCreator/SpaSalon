from core.forms import BootstrapControlForm
from reviews.models import Reviews


class ReviewsForm(BootstrapControlForm):
    class Meta:
        model = Reviews
        exclude = ("user", "is_published")
