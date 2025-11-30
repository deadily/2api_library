from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Author(models.Model):
    full_name = models.CharField(max_length=255, unique=True, verbose_name="ФИО Автора")
    biography = models.TextField(blank=True, verbose_name="Биография")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"


class Book(models.Model):
    CATEGORY_CHOICES = [
        ('fiction', 'Художественная литература'),
        ('textbook', 'Учебник'),
    ]

    title = models.CharField(max_length=100, verbose_name="Название книги")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books', verbose_name="Автор")
    publication_year = models.IntegerField(
        validators=[MinValueValidator(1000), MaxValueValidator(9999)],
        verbose_name="Год выпуска"
    )
    genre = models.CharField(max_length=100, verbose_name="Жанр")
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, verbose_name="Категория")
    publisher = models.CharField(max_length=100, verbose_name="Издательство")

    cover_image = models.ImageField(upload_to='covers/', verbose_name="Обложка", blank=True, null=True)
    book_file = models.FileField(upload_to='books/', verbose_name="Файл книги")

    def __str__(self):
        return f"{self.title} ({self.publication_year})"

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
        unique_together = ['title', 'author', 'publication_year', 'publisher']