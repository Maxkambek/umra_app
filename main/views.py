from .serializers import NewsSerializer
from .models import News
from rest_framework import generics


class NewsListAPIView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
