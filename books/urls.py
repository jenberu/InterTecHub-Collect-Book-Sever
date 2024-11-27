from django.urls import path
from .views import BookAPIView,mark_favorite,book_recommendations,home

urlpatterns = [
 path('', home, name='home'),  

    path('books/', BookAPIView.as_view(),name='book-list'),
    path('books/<int:pk>/', BookAPIView.as_view(),name='book-detail'),
    path('books/recommendations/', book_recommendations, name='book-recommendation'),
    path('books/favorite/', mark_favorite, name='mark-favorite'),
]