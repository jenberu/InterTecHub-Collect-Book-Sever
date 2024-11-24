from django.urls import path
from .views import BookAPIView

urlpatterns = [
    path('', BookAPIView.as_view(),name='book-list'),
    path('api/books/<int:pk>/', BookAPIView.as_view(),name='book-detail'),
]