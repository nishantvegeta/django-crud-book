from django.urls import path
from .views import index, book_list, book_by_id, create_book, update_book, delete_book 
from crudapp import views

urlpatterns = [
    path('', index, name="index"),
    path('book/', book_list, name="book"),
    path('book/<int:id>/', book_by_id , name="id"),
    path('create/', create_book, name="create"),
    path('update/<int:id>', update_book, name="update"),
    path('delete/<int:id>', delete_book, name="delete"),
    path('crudapp/', views.Schoollist.as_view()),
    path('crudapp/<int:id>/', views.Schoollistdetails.as_view()),
]
