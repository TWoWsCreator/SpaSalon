import django.contrib.auth.views
from django.urls import path, re_path, reverse_lazy

from users.views import SignUpView, PasswordReset, ProfileView

app_name = "users"

urlpatterns = [
    path(
        "login/",
        django.contrib.auth.views.LoginView.as_view(
            template_name="users/login.html",
        ),
        name="login",
    ),
    path("sign_up/", SignUpView.as_view(), name="sign_up"),
    path(
        "password_change/done/",
        django.contrib.auth.views.PasswordChangeDoneView.as_view(
            template_name="users/password_change_done.html"
        ),
        name="password_change_done",
    ),
    path(
        "password_change/",
        django.contrib.auth.views.PasswordChangeView.as_view(
            template_name="users/password_change.html",
            success_url=reverse_lazy("users:password_change_done"),
        ),
        name="password_change",
    ),
    path(
        "password_reset/",
        PasswordReset.as_view(),
        name="password_reset",
    ),
    path(
        "password_reset/done/",
        django.contrib.auth.views.PasswordResetDoneView.as_view(
            template_name="users/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    re_path(
        r"password_reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$",
        django.contrib.auth.views.PasswordResetConfirmView.as_view(
            template_name="users/password_reset_confirm.html",
            success_url=reverse_lazy("users:password_reset_complete"),
        ),
        name="password_reset_confirm",
    ),
    path(
        "password_reset/complete/",
        django.contrib.auth.views.PasswordResetCompleteView.as_view(
            template_name="users/password_reset_complete.html",
        ),
        name="password_reset_complete",
    ),
    path("profile/", ProfileView.as_view(), name="profile"),
]
