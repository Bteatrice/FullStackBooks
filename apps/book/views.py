
from django.shortcuts import render, redirect
from .models import Book
# Create your views here.
def index(request):
    context = {
        "books": Book.objects.all()
    }
    return render(request, "book/index.html", context)

def books(request):
    # using ORM
    Book.objects.create(title=request.POST['title'], author=request.POST['author'], category=request.POST['category'])
    #insert into Book(title, author, category, creates_at, updated_at) values (title, author, category, now(), now())
    return redirect('/')

def remove(request, id):
    book = Book.objects.filter(id=id)
    book.delete()

    return redirect('/')
