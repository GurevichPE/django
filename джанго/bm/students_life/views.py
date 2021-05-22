from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import generics

from students_life.models import Book, Library, BookInLib
from students_life.serializers import BookSerializer, LibrarySerializer, BookInLibSerializer


class BookList(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = Book.objects.all()
        pages = self.request.query_params.get('pages_amount', None)
        pages = int(pages)

        for book in queryset:
            if int(book.pages) > pages:
                print(str(book.name))
    serializer_class = BookSerializer


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class LibList(generics.ListCreateAPIView):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer


class LibDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer


class BookInLibDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookInLib.objects.all()
    serializer_class = BookInLibSerializer


class BookInLibList(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = BookInLib.objects.all()
        name = self.request.query_params.get('name', None)
        bookname = self.request.query_params.get('book', None)

        try:
            name = name.upper()
        except BaseException:
            name = '//'

        try:
            bookname = bookname.upper()
        except BaseException:
            bookname = '//'

        book_name = Book.objects.filter(
            name__contains=name).first()

        exact = Book.objects.filter(
            name__contains=bookname).first()

       # exact = BookInLib.objects.all()
        try:
            for boook in queryset:
                if boook.book.name == book_name.name:
                    print('book ' + str(book_name) + str(boook.id) + ' from ' + str(boook.lib) +
                          ' was taken by students ' + str(boook.students) + ' times')
        except AttributeError:
            pass

        if type(exact) != None:
            for boook in queryset:
                if boook.book.name == exact.name:
                    print('book ' + str(book_name) + str(boook.id) + ' from ' + str(boook.lib) +
                          ' was taken by ' + str(boook.departments) + ' departments')

        return queryset

    serializer_class = BookInLibSerializer

