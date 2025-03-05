from django.core.validators import FileExtensionValidator
from django.db import models
from ..courses.models import Course
from ..config.settings import AUTH_USER_MODEL


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=True, null=True)
    lesson_number = models.IntegerField(verbose_name='номер урока')
    title = models.CharField(max_length=100, verbose_name='название урока')
    description = models.TextField(verbose_name='описание урока', max_length=1000)
    video = models.FileField(upload_to='videos_uploaded', null=True,
                             validators=[
                                 FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])
    create_at = models.DateField(verbose_name='дата создания', auto_now_add=True)
    update_at = models.DateField(verbose_name='дата обновления', auto_now=True)
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} - {self.course} - {self.title}"

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"


class ProgressionSystem(models.Model):
    student = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    date_end = models.DateField(verbose_name='дата завершения',)

    def __str__(self):
        return f"{self.student.email} - {self.lesson.title} - {self.date_end}"

    class Meta:
        verbose_name = 'Система прогрессии'
        verbose_name_plural = 'Системы прогрессии'