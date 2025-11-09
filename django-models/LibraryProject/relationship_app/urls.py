from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.get_all_books, name='all_books'),
    path('library/<int:pk>/', views.LibraryDetailsView.as_view(), name='library_books'),
]