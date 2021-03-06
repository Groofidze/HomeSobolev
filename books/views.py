from django.views.generic import ListView
from books.models import Books


class Index(ListView):
    template_name = "books/index.html"
    model = Books
    context_object_name = "books"
