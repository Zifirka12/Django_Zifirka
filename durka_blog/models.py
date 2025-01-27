from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    # Поле для статуса публикации
    is_published = models.BooleanField(default=False)

    name = models.CharField(
        max_length=100,
        verbose_name="Заголовок",
        help_text="Введите заголовок поста",
    )
    description = models.TextField(
        verbose_name="Содержание",
        help_text="Введите содержание поста",
        blank=True,
        null=True,
    )
    image = models.ImageField(
        upload_to="post/image",
        blank=True,
        null=True,
        verbose_name="Превью",
        help_text="Вставьте изображение для поста",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
        help_text="Введите дату создания",
    )
    was_publication = models.BooleanField(
        default=True, verbose_name="Опубликован пост", help_text="Опубликован пост?"
    )
    views_counter = models.PositiveIntegerField(
        verbose_name="Количество просмотров",
        help_text="Введите количество просмотров",
        default=0,
    )

    class Meta:
        permissions = [
            ("can_unpublish_post", "Может отменять публикацию поста"),
        ]
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ["-created_at"]  # Упрощено сортировка

    def __str__(self):
        return self.name
