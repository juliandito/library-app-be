from rest_framework import generics
from library.models import Book
from library.serializers import BookSerializer, BookLikeSerializer


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookLikeList(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookLikeSerializer
