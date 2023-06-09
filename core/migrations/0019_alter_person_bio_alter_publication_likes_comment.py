# Generated by Django 4.2.1 on 2023-06-05 08:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0018_publication_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='bio',
            field=models.TextField(blank=True, verbose_name='Текст биографии'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='publication_likes', to=settings.AUTH_USER_MODEL, verbose_name='Лайки публикации'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(verbose_name='Тело комментария')),
                ('image', models.ImageField(blank=True, upload_to='photos/comments/%Y/%m/%d/', verbose_name='Фото комментария')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Время и дата комментария')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='core.comment', verbose_name='parent comment')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_profile', to='core.profile', verbose_name='Комментатор')),
                ('publication', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_publications', to='core.publication', verbose_name='Публикация комментария')),
            ],
            options={
                'verbose_name': 'Комментарий',
            },
        ),
    ]
