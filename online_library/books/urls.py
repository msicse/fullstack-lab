from django.urls import path
from . import views

urlpatterns = [
    path("", views.book_list, name="book-list"),
    path("books/", views.books_only_list, name="books-list"),
    path("books/<int:pk>/", views.book_detail, name="book-detail"),
]