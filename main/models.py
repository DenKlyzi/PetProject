from django.db import models


class TelegramUser(models.Model):
    user_id = models.PositiveIntegerField(verbose_name = 'Telegram ID')
    user_name = models.CharField(max_length = 50, verbose_name = 'Логин')
    first_name = models.CharField(max_length = 50, verbose_name = 'Имя')
    group = models.CharField(max_length = 25, verbose_name = 'Команда')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.user_name
