# Generated by Django 2.2.16 on 2022-03-29 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20220329_1145'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='follow',
            name='following_unique',
        ),
        migrations.RenameField(
            model_name='follow',
            old_name='author',
            new_name='following',
        ),
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.UniqueConstraint(fields=('user', 'following'), name='following_unique'),
        ),
    ]