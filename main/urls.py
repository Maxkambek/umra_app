from .views import NewsListAPIView
from django.urls import path

urlpatterns = [
    path('', NewsListAPIView.as_view())
]
