from django.contrib import admin
from books.models import Books


@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
    fields = [
        'name',
        'chapter',
        'price',
    ]
    ordering = [
        'name',
    ]
