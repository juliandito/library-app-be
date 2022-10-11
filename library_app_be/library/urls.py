from django.urls import path
from library import views

urlpatterns = [
    path('api/books', views.BookList.as_view()),
    path('api/books/likes', views.BookLikeList.as_view()),
]