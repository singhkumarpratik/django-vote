from django.contrib.auth.models import User
from django import forms
from .models import User


class LoginForm(forms.Form):
    email = forms.EmailField(label="Enter email")
    password = forms.CharField(label="Enter password", widget=forms.PasswordInput)

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        try:
            user = User.objects.get(username=email)
            if user.check_password(password):
                return self.cleaned_data
            else:
                self.add_error("password", forms.ValidationError("Password Incorrect"))
        except:
            self.add_error("email", forms.ValidationError("User Doesn't Exist"))

        return email

    def save(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
