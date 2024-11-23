# Generated by Django 4.2.2 on 2024-11-18 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Blog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=40, verbose_name="Заголовок")),
                (
                    "topik",
                    models.TextField(max_length=100, verbose_name="Содержимое статьи"),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        help_text="Загрузите фото",
                        null=True,
                        upload_to="blog/",
                        verbose_name="Изображение",
                    ),
                ),
                (
                    "number_of_views",
                    models.IntegerField(
                        default=0, verbose_name="количество просмотров"
                    ),
                ),
                (
                    "date_of_publication",
                    models.DateField(auto_now_add=True, verbose_name="Дата публикации"),
                ),
                (
                    "is_published",
                    models.BooleanField(default=True, verbose_name="Опубликовано"),
                ),
            ],
            options={
                "verbose_name": "Статья",
                "verbose_name_plural": "Статьи",
                "ordering": ("title",),
            },
        ),
    ]
