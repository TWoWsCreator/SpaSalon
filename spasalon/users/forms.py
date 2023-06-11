from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from core.forms import BootstrapControlForm
from users.models import CustomUser, PasswordResetEmail


class CustomUserCreationForm(UserCreationForm, BootstrapControlForm):
    class Meta:
        model = CustomUser
        fields = (
            "username",
            "email",
        )


class CustomUserChangeForm(UserChangeForm, BootstrapControlForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserChangeForm, self).__init__(*args, **kwargs)
        instance = getattr(self, "instance", None)
        if instance and instance.pk:
            self.fields["username"].widget.attrs["readonly"] = True
            self.fields["email"].widget.attrs["readonly"] = True

    class Meta:
        model = CustomUser
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
        )
        readonly_fields = ["username", "email"]


class PasswordResetEmailForm(BootstrapControlForm):
    class Meta:
        model = PasswordResetEmail
        fields = ("user_email",)
