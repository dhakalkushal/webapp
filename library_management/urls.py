from django.urls import path, include
from . import views
#from comments.views import CommentCreate

urlpatterns = [
    path('book/',views.ListBooks.as_view(), name = 'book-index'),
    path('book/<str:pk>/', views.book_detail, name = 'book-detail'),
    path('book/<str:pk>/edit/',views.UpdateBook.as_view(), name = 'book-update'),
    path('book/<str:pk>/request/',views.request_borrow, name = 'borrow-request'),
    path('borrower/', views.ListBorrowers.as_view(), name='borrower-index'),
    path('borrower/<str:pk>/return/', views.return_book, name = 'borrow-return'),
    path('student/', views.ListStudent.as_view(), name='student-index'),
    path('student/<str:pk>/', views.student_detail, name = 'student-detail'),
    path('student/<str:pk>/edit/', views.UpdateStudent.as_view(), name = 'student-update'),
]