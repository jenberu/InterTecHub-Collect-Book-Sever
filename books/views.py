from django.shortcuts import render

from .serializers import BookSerialzer
from .models import Bookes
from rest_framework.response import Response
from rest_framework.views import APIView

class BookAPIView(APIView):
    serializer_class = BookSerialzer

    def get(self, request):
        books = Bookes.objects.all()
        serializer = self.serializer_class(books, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    def put(self, request, pk):
        book = Bookes.objects.get(pk=pk)
        serializer = self.serializer_class(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    def delete(self, request, pk):
        book = Bookes.objects.get(pk=pk)
        book.delete()
        return Response(status=204)
