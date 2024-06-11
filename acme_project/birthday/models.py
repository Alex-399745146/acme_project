# birthday/models.py
from django.db import models

# Импортируется функция-валидатор.
from .validators import real_age


class Birthday(models.Model):
    first_name = models.CharField(
        'Имя',
        max_length=20
    )
    last_name = models.CharField(
        'Фамилия',
        blank=True,  # Допустимы пустые значения.
        help_text='Необязательное поле',
        max_length=20
    )
    birthday = models.DateField(
        'Дата рождения',
        validators=(real_age,)
    )
    image = models.ImageField(
        'Фото',
        upload_to='birthdays_images',
        blank=True
    )

    class Meta:
        ordering = ('id',)
        # Проверка на уникальность записей.
        constraints = (
            models.UniqueConstraint(
                fields=('first_name', 'last_name', 'birthday'),
                name='Unique person constraint',
            ),
        )
