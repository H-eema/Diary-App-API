from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from .models import Diary
from .serializers import DiarySerializer


class DiaryListView(ListCreateAPIView):
    serializer_class = DiarySerializer

    def get_queryset(self):
        queryset = Diary.objects.filter(writer=self.request.user).order_by("-date")

        return queryset


class DiaryDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Diary.objects.all()
    serializer_class = DiarySerializer
