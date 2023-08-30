from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm,
    AuthenticationForm,
)

from django import forms
from .models import WodRecord


class WodRecordForm(forms.ModelForm):
    class Meta:
        model = WodRecord
        fields = ("wod_name", "record", "date")


class CustomUserCreationForm(UserCreationForm):
    nickname = forms.CharField(max_length=8, required=True)  # 닉네임 필드 추가

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = (
            "username",
            "email",
            "nickname",
            "first_name",
            "last_name",
            "password1",
            "password2",
            "profile_image",
        )


class CustomUserChangeForm(UserChangeForm):
    password = None

    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = (
            "email",
            "nickname",
            "first_name",
            "last_name",
            "profile_image",
        )


class CustomAuthenticationForm(AuthenticationForm):
    pass
