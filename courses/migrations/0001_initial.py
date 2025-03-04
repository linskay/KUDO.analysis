# Generated by Django 5.1.6 on 2025-03-04 14:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('name_course', models.CharField(max_length=150, verbose_name='Название курса')),
                ('description_course', models.TextField(blank=True, null=True, verbose_name='Описание курса')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания курса')),
                ('update_date', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата изменения курса')),
                ('photo_course', models.ImageField(blank=True, null=True, upload_to='courses_photos/', verbose_name='Фото превью')),
                ('pay_course', models.BooleanField(blank=True, default=False, null=True)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['name_course'],
            },
        ),
        migrations.CreateModel(
            name='CourseAndStudents',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('course_completion', models.IntegerField(default=0, verbose_name='процент завершения курса')),
                ('finish_date', models.DateTimeField(blank=True, default=None, null=True, verbose_name='Дата окончания курса')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course', to='courses.course')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'course')},
            },
        ),
        migrations.AddField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(blank=True, related_name='students', through='courses.CourseAndStudents', to=settings.AUTH_USER_MODEL),
        ),
    ]
