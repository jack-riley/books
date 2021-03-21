from django.urls import path
from . import views
urlpatterns =[
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('books', views.books),
    path('book/<int:id>', views.book_detail),
    path('new_book', views.process_book),
    path('favorite', views.process_like_1),
    path('favorite_2', views.process_like_2),
    path('unfavorite', views.remove_like),
    path('edit_book/<int:id>', views.edit),
    path('logout', views.logout),
    path('delete', views.delete)


]