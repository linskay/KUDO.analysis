from django.db import models
from users.models import User
import datetime
# Create your models here.
"""class CourseCategory(models.Model):

    id = models.AutoField(primary_key=True, verbose_name="id")
    name_course_category = models.CharField(max_length=150, unique=True, verbose_name="Категория курса")
    description_course_category =  models.TextField(verbose_name="Описание категории курсов", null=True, blank=True,)

    def __str__(self):
        return self.name_course_category

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name_course_category']"""



class Course(models.Model):
    """ Модель Курсы"""
    id = models.AutoField(primary_key=True, verbose_name="id")
    #category = models.ForeignKey(CourseCategory,  on_delete=models.CASCADE, related_name="category")
    name_course = models.CharField(max_length=150, verbose_name="Название курса")
    description_course = models.TextField(verbose_name="Описание курса", null=True, blank=True,)
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания курса")
    update_date = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name="Дата изменения курса")
    photo_course = models.ImageField(upload_to='courses_photos/',  null=True, blank=True, verbose_name="Фото превью")
    like_counter =models.IntegerField(null=True, blank=True, verbose_name="Лайки")

    #teacher = models.ManyToManyField(User, related_name="teacher")
    pay_course = models.BooleanField(default=False,null=True, blank=True,)
    students = models.ManyToManyField(User, blank=True,  through="CourseAndStudents", related_name="students")

    def __str__(self):
        return self.name_course

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name_course']


class CourseAndStudents(models.Model):
    """ Связующая таблица для связки Курсы - Студенты"""
    id = models.AutoField(primary_key=True, verbose_name="id")
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, )
    course = models.ForeignKey(Course, on_delete=models.CASCADE, )
    course_completion = models.IntegerField(default=0, verbose_name="процент завершения курса")
    finish_date = models.DateTimeField(default=datetime.datetime(1900,1,1),  verbose_name="Дата окончания курса")

    def __str__(self):
        return f"{self.course} - {self.user}"

    class Meta:
        unique_together = [('user', 'course')]
