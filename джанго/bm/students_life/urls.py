from django.urls import path

from students_life.views import BookList, BookDetail, LibDetail, LibList, BookInLibDetail, BookInLibList

urlpatterns = [
    path('book/', BookList.as_view()),
    path('book/<int:pk>/', BookDetail.as_view()),
    path('library/', LibList.as_view()),
    path('library/<int:pk>/', LibDetail.as_view()),
    path('book_in_lib/', BookInLibList.as_view()),
    path('book_in_lib/<int:pk>/', BookInLibDetail.as_view()),
    ]