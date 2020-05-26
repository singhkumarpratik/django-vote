from django.shortcuts import render
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import FormView
from .forms import LoginForm


class UserLoginView(FormView):
    form_class = LoginForm
    template_name = "users/login.html"
    success_url = reverse_lazy("home:comment")

    def form_valid(self, form):
        form.save()
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)


def logout_request(request):
    logout(request)
    return redirect("home:comment")
