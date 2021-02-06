from django.urls import path
from . import views

#write all pathes for all pages in  this app
urlpatterns = [
    
    path('',views.index, name='index'),
    path('books',views.books, name='books'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
]