# Generated by Django 3.2.6 on 2021-09-18 23:27

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='درباره ی من'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('خانم', 'خانم'), ('آقا', 'آقا'), ('دیگری', 'دیگری')], default='دیگری', max_length=6, verbose_name='جنسیت'),
        ),
    ]
