from . import views
from django.urls import path
from myapp.views import BookListCreateView
urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    
    
]
