from datetime import timezone
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
        date_param = self.request.query_params.get("date_param")

        if date_param:
            queryset = queryset.filter(date__date=date_param)

        return queryset


class DiaryDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Diary.objects.all()
    serializer_class = DiarySerializer
