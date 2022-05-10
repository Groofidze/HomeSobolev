from django.db import models


class ChapterBooks(models.Model):
    name = models.CharField(verbose_name="Название жанра", max_length=128)
    tag_alib = models.CharField(verbose_name="Тег алиба", max_length=128)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ["name"]
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"


class Books(models.Model):
    name = models.CharField(verbose_name="Название книги", max_length=128)
    chapter = models.ForeignKey(ChapterBooks, on_delete=models.CASCADE, verbose_name="Жанр", default=1)
    price = models.PositiveIntegerField(verbose_name="Цена")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ["name"]
        verbose_name = "Книгу"
        verbose_name_plural = "Книги"
