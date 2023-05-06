from django.shortcuts import redirect, render
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import Book
from myapp.Serializer import BookSerializer
from myapp.form import BookForm


# Create your views here.



class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    template_name = 'books.html'
    form_class = BookForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        books = Book.objects.all()
        return render(request, self.template_name, context= {'form': form, 'books': books})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            books = Book.objects.all()
            return redirect('/./books/', {'books': books})
        else:
            return render(request, self.template_name, {'form': form})
        

    

    