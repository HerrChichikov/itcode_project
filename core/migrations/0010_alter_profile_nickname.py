# Generated by Django 4.2.1 on 2023-06-03 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_categories_options_alter_person_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='nickname',
            field=models.CharField(blank=True, default='Анон', max_length=255, verbose_name='Никнейм профиля'),
        ),
    ]