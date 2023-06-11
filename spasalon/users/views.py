from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.contrib.messages import error
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.views.generic import CreateView, FormView

from users.forms import (
    CustomUserChangeForm,
    CustomUserCreationForm,
    PasswordResetEmailForm,
)
from users.models import CustomUser, PasswordResetEmail


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("users:login")
    template_name = "users/sign_up.html"

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


class ProfileView(LoginRequiredMixin, FormView):
    template_name = "users/profile.html"
    form_class = CustomUserChangeForm
    success_url = reverse_lazy("users:profile")

    def get_form(self):
        return self.form_class(
            self.request.POST or None,
            self.request.FILES,
            instance=self.request.user,
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.form_class(
            initial=self.initial,
            instance=self.request.user,
        )
        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class PasswordReset(FormView):
    template_name = "users/password_reset.html"
    model = PasswordResetEmail
    form_class = PasswordResetEmailForm

    def form_valid(self, form):
        user_email = form.cleaned_data["user_email"]
        try:
            user = CustomUser.objects.get(email=user_email)
        except CustomUser.DoesNotExist:
            error(
                self.request,
                "Введите почту, которую вводили при регистрации на сайте.",
            )
            return redirect(reverse_lazy("users:password_reset"))
        token = default_token_generator.make_token(user)
        msg_data = {
            "mail": user.email,
            "protocol": "http",
            "domain": "127.0.0.1:8000",
            "uid": urlsafe_base64_encode(force_bytes(user.pk)),
            "token": token,
        }
        send_mail(
            'Сброс пароля',
            f'{msg_data}',
            'example@mail.ru',
            [user.email],
            fail_silently=True,
        )
        return redirect(reverse_lazy("users:password_reset_done"))
