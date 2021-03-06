# Generated by Django 3.2.6 on 2021-09-14 18:05

import Blog.utils
from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(allow_unicode=True, null=True, unique=True)),
                ('m_time', django_jalali.db.models.jDateTimeField(auto_now_add=True, verbose_name='تاریخ عضویت ')),
                ('edit_date', django_jalali.db.models.jDateTimeField(auto_now_add=True, verbose_name='تاریخ آخرین ویرایش ')),
                ('title', models.CharField(max_length=50, verbose_name='عنوان')),
                ('su_des', models.CharField(max_length=300, verbose_name='توضیحات خلاصه')),
                ('co_des', models.TextField(verbose_name='توضیحات کامل')),
                ('state', models.PositiveSmallIntegerField(choices=[(2, 'تایید'), (1, 'در حال بررسی'), (0, 'عدم تایید')], default=2, verbose_name='وضعیت')),
                ('category', models.PositiveSmallIntegerField(choices=[(2, 'علمی'), (1, 'آموزشی  '), (0, 'خبری ')], default=0, verbose_name='دسته بندی')),
                ('height', models.IntegerField(blank=True, null=True)),
                ('width', models.IntegerField(blank=True, null=True)),
                ('img', models.ImageField(height_field='height', null=True, upload_to=Blog.utils.post_image_path, width_field='width')),
                ('author', models.ManyToManyField(blank=True, related_name='posts', to='Account.Profile', verbose_name='نویسنده ')),
            ],
            options={
                'verbose_name': 'پست',
                'verbose_name_plural': 'پست ها',
                'ordering': ['m_time'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m_time', django_jalali.db.models.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('comment', models.TextField(verbose_name=' دیدگاه')),
                ('state', models.PositiveSmallIntegerField(choices=[(2, 'تایید'), (1, 'در حال بررسی'), (0, 'عدم تایید')], default=1, verbose_name='وضعیت')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Blog.post', verbose_name='عنوان پست ')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Account.profile', verbose_name=' نام کاربر')),
            ],
            options={
                'verbose_name': 'کامنت',
                'verbose_name_plural': 'کامنت ها',
                'ordering': ['-m_time'],
            },
        ),
    ]
