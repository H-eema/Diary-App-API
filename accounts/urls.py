from django.urls import path, include

from dj_rest_auth.views import PasswordResetConfirmView


urlpatterns = [
    path("", include("dj_rest_auth.urls")),
    path("registration/", include("dj_rest_auth.registration.urls")),
    path(
        "password/reset/confirm/<str:uid>/<str:token>/",
        PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
]
