from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import generics

from students_life.models import Book, Library, BookInLib
from students_life.serializers import BookSerializer, LibrarySerializer, BookInLibSerializer


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
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

        try:
            name = name.upper()
        except BaseException:
            name = ''

        print(name, type(name))


        book_name = Book.objects.filter(
            name__contains=name).first()  # все вхождение, которое встретил ORM при обращении к БД
        exact = BookInLib.objects.all()
        for boook in exact:
            if boook.book.name == book_name.name:
                print('book ' + str(book_name) + str(boook.id) + ' from ' + str(boook.lib) + ' was taken by students ' + str(boook.students) + ' times')
        print('------------------------------------------------------')



       # for book in students_queryset:
     #       the_student_in_room = BookInLib.objects.filter(id=book.id).first()
     #       print(the_student_in_room)
     #       print('for in for')
          #  rooms_capacity_of_this_student = BookInLib.objects.filter(id=book.id).filter(room__capacity=capacity).all()
       #     for room_capacity in rooms_capacity_of_this_student:
         #       print(room_capacity)

        print('-------------------++++++++++++++++++-----------------')
        return queryset

    serializer_class = BookInLibSerializer

# class WormList(generics.ListCreateAPIView):
#     def get_queryset(self):
#         queryset = Worm.objects.all()
#
#         symbols = self.request.query_params.get('symbols', None)
#         if symbols is not None:
#             try:
#                 # symbols = symbols.upper()
#                 # symbols = symbols.replace('Ч', 'ч')
#                 # symbols = symbols.replace('Е', 'е')
#
#                 queryset = queryset.filter(name__icontains=symbols).order_by('name')
#             except ValueError:
#                 pass
#         return queryset
#
#     serializer_class = WormSerializer
