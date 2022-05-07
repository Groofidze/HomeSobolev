from django.db import models


class Books(models.Model):
    ENG_FANTASY = "tzfant"
    RUS_FANTASY = "tofant"
    SECOND_WORLD_WAR = "t2mv"
    ADD_GENRE = "Добавить жанр"

    TYPE_GENRES = (
        [ADD_GENRE, ADD_GENRE],
        [ENG_FANTASY, "Фантастика зарубежная"],
        [RUS_FANTASY, "Фантастика отечественная"],
        [SECOND_WORLD_WAR, "Вторая мировая война"],
    )

    name = models.CharField(verbose_name="Название книги", max_length=128)
    chapter = models.CharField(verbose_name="Жанр", choices=TYPE_GENRES, default=ADD_GENRE, max_length=64)
    price = models.PositiveIntegerField(verbose_name="Цена")
