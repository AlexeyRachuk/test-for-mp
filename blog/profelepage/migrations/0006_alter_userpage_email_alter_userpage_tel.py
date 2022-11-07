# Generated by Django 4.1.3 on 2022-11-07 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profelepage', '0005_alter_userpage_email_alter_userpage_map_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpage',
            name='email',
            field=models.CharField(default='Добавить код через источник', max_length=100, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='userpage',
            name='tel',
            field=models.CharField(help_text='Добавить код через источник', max_length=100, verbose_name='Телефон'),
        ),
    ]
