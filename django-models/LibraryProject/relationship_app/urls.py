from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import list_books, LibraryDetailView
from . import views



urlpatterns = [
#    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('books/', list_books, name='all_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_books'),
    path('admin-page/', views.admin_view, name='admin_page'),
    path('librarian-page/', views.librarian_view, name='librarian_page'),
    path('member-page/', views.member_view, name='member_page'),
    path('books/add/', views.add_book, name='add_book'),
    path('books/edit/<int:pk>/', views.edit_book, name='edit_book'),
    path('books/delete/<int:pk>/', views.delete_book, name='delete_book'),
]