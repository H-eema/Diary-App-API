from django.urls import path

from .views import DiaryListView, DiaryDetailView

urlpatterns = [
    path("mydiaries/", DiaryListView.as_view(), name="diary-list"),
    path("mydiaries/<int:pk>/", DiaryDetailView.as_view(), name="diary-detail"),
]
