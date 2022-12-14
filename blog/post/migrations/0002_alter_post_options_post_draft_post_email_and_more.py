# Generated by Django 4.1.3 on 2022-11-07 08:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Блог', 'verbose_name_plural': 'Блог'},
        ),
        migrations.AddField(
            model_name='post',
            name='draft',
            field=models.BooleanField(default=False, help_text='Определяет будет ли опубликаван пост', verbose_name='Публикация'),
        ),
        migrations.AddField(
            model_name='post',
            name='email',
            field=models.CharField(default=1, help_text='Оформить по примеру: <a href="mailto:Email">Email</a>', max_length=100, verbose_name='Email'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='main_text',
            field=models.TextField(default=1, help_text='Для наполнения перейти в источник', verbose_name='Основной текст'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='photo_prew',
            field=models.ImageField(default=1, upload_to='images/', verbose_name='Фото превью'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='postdate',
            field=models.DateField(default=datetime.date.today, verbose_name='Дата публикации'),
        ),
        migrations.AddField(
            model_name='post',
            name='tel',
            field=models.CharField(default=1, help_text='Оформить по примеру: <a href="tel:Номер телефон с +7 и слитно">Номер телефона</a>', max_length=100, verbose_name='Телефон'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='text_prew',
            field=models.TextField(default=1, verbose_name='Превью статьи'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default=1, max_length=100, verbose_name='Заголовок статьи'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='url',
            field=models.SlugField(default=1, help_text='Латиницей, разделитель (_), должен быть уникальный!', unique=True, verbose_name='URL поста'),
            preserve_default=False,
        ),
    ]
