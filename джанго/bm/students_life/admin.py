from django.contrib import admin

# Register your models here.
from students_life.models import Book, Library, BookInLib

admin.site.register(Book)
admin.site.register(Library)
admin.site.register(BookInLib)