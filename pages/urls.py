from django.urls import path
from .views import * 

urlpatterns = [
    path('', Homepage.as_view(), name="home"),
    path('about/', AboutPage.as_view(), name = "about"),
    path('contact/', ContactPage.as_view(), name = "contact"),
    path('myteam/', MyTeamPage.as_view(), name = "myteam"),
    path('reklama/', ReklamaPage.as_view(), name = "reklama"),
    path('books/', BooksPage.as_view(), name="books"),
    path('books<int:pk>/', BookDetailPage.as_view(), name='book_detail'),
]