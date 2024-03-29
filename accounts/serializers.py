from dj_rest_auth.registration.serializers import (
    RegisterSerializer,
)
from dj_rest_auth.serializers import PasswordResetConfirmSerializer
from rest_framework import serializers

from .models import CustomUser


class CustomRegisterSerializer(RegisterSerializer):
    full_name = serializers.CharField()
    age = serializers.IntegerField()
    occupation = serializers.CharField()

    class Meta:
        model = CustomUser
        fields = (
            "email",
            "password1",
            "password2",
            "full_name",
            "username",
            "age",
            "occupation",
        )

    def custom_signup(self, request, user):
        pass


class CustomPasswordResetConfirmSerializer(PasswordResetConfirmSerializer):

    def __init__(self, *args, **kwargs):
        context = kwargs.get("context", {})
        url_kwargs = context.get("view").kwargs

        self.fields["uid"] = serializers.CharField(
            max_length=100, required=True, initial=url_kwargs.get("uid")
        )
        self.fields["token"] = serializers.CharField(
            max_length=100, required=True, initial=url_kwargs.get("token")
        )

        super(CustomPasswordResetConfirmSerializer, self).__init__(*args, **kwargs)
