# Generated by Django 4.2.1 on 2023-06-05 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_alter_person_bio_alter_publication_likes_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='level',
            new_name='Ответ комментарию #',
        ),
    ]
