# Generated by Django 3.2.6 on 2021-09-19 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0003_alter_post_co_des'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment',
            new_name='message',
        ),
    ]