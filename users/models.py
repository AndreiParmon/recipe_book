from django.conf import settings
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_birth = models.DateField(blank=True, null=True)
    avatar = models.ImageField(upload_to='images/', default='default.png', blank=True, null=True,
                               verbose_name='Фото профиля')

    class Meta:
        """
        Сортировка, название таблицы в базе данных
        """
        verbose_name = 'Автора'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        """
        Возвращение строки
        """
        return self.user.username
