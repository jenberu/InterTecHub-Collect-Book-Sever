from django.shortcuts import render

from .serializers import BookSerialzer
from .models import Book
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404 ,render
from rest_framework import status
from rest_framework.decorators import api_view
import random
from django.http import HttpResponse

def home(request):
    try:
        books=Book.objects.all()
        return render(request,'home.html',{'books':books})

    except Book.DoesNotExist:   
            return render(request,'home.html')


class BookAPIView(APIView):
    serializer_class = BookSerialzer

    def get(self, request,pk=None):
        try:
            if pk:
                book = get_object_or_404(Book,pk=pk)
                serializer = self.serializer_class(book)
                return Response(serializer.data,status=status.HTTP_200_OK)
            
            books = Book.objects.all()
            serializer = self.serializer_class(books, many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Book.DoesNotExist:
            return Response(
                {"error": "Book not found."}, status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {"error": "An unexpected error occurred: " + str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
        
    def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {"error": "An unexpected error occurred: " + str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    
    def put(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
            serializer = self.serializer_class(book, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Book.DoesNotExist:
            return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    
    def delete(self, request, pk=None):
        try:
                
            book = Book.objects.get(pk=pk)
            book.delete()
            return Response({"message": "Book deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Book.DoesNotExist:
            return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
def book_recommendations(request):
    try:
        books = Book.objects.all()    
        if books.exists():
            book = random.choice(books)
            serializer = BookSerialzer(book)
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response({"detail": "No books found."}, status=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        return Response(
            {"error": f"An unexpected error occurred: {str(e)}"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
@api_view(['POST'])
def mark_favorite(request):
    try:
        book_id=request.data.get('book_id')
        book = Book.objects.get(pk=book_id)
        book.is_favorite=True
        book.save()
        return Response({"message": "Book Marked as favorite"}, status=status.HTTP_200_OK)
    except Book.DoesNotExist:
        return Response({"detail": "use {book_id:<id>}  format  in content section"}, status=status.HTTP_404_NOT_FOUND)





