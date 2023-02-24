from django.shortcuts import render
from rest_framework import generics
from core.models import Books
from .serializers import BookSerializer
# Create your views here.

class BookApiView(generics.ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer