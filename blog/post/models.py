from django.contrib.auth.models import User
from datetime import date
from django.db import models
from django.urls import reverse


class Post(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.PROTECT)
    title = models.CharField('Заголовок статьи', max_length=100)
    url = models.SlugField('URL поста', unique=True, help_text='Латиницей, разделитель (_), должен быть уникальный!')
    text_prew = models.TextField('Превью статьи')
    photo_prew = models.ImageField('Фото превью', upload_to='images/')
    postdate = models.DateField('Дата публикации', default=date.today)
    main_text = models.TextField('Основной текст', help_text='Для наполнения перейти в источник')
    draft = models.BooleanField('Публикация', default=False, help_text='Определяет будет ли опубликаван пост')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.url})

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блог"
