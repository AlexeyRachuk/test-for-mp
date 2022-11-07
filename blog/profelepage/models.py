from django.contrib.auth.models import User
from django.db import models


class UserPage(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.PROTECT, null=True)
    map = models.TextField('Карта',
                           help_text='Сгенерировать яндекс-карту с любой меткой и вставить сюда через источник',
                           default=1)
    tel = models.CharField('Телефон', max_length=100, help_text='Добавить код через источник')
    email = models.CharField('Email', max_length=100, default='Добавить код через источник')

    def __str__(self):
        return self.user.first_name

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профиль"
