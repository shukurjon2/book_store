from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from .models import *

# Create your views here.

class Homepage(ListView):
    model = Blog
    template_name = "index.html"
   

class AboutPage(TemplateView):
    template_name = "about.html"

class ContactPage(CreateView):
    model = Data
    template_name = "contact.html"
    fields = "__all__"

class MyTeamPage(TemplateView):
    template_name = "my_team.html"

class ReklamaPage(TemplateView):
    template_name = "reklama.html"

class BooksPage(ListView):
    model = Book 
    template_name = "books.html"

class BookDetailPage(DetailView):
    model = Book
    template_name = "book_detail.html"