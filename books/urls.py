from django.urls import path
from .views import BookAPIView

urlpatterns = [
    path('books/', BookAPIView.as_view()),
    path('books/<int:pk>/', BookAPIView.as_view()),
]