from rest_framework import serializers

from students_life.models import Book, Library, BookInLib


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'  # ['fio','group']
        model = Book


class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Library



class BookInLibSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = BookInLib
