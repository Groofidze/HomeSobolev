from django.contrib import admin
from books.models import Books, ChapterBooks


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

    def get_queryset(self, request):
        return Books.objects.select_related("chapter").all()


@admin.register(ChapterBooks)
class ChapterBooksAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
    fields = [
        'name',
        'tag_alib',
    ]
    ordering = [
        'name',
    ]
