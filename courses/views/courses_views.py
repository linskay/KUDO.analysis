from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from ..models import Course, CourseAndStudents, User
from django.views.generic import ListView, DetailView
from ..forms import CoursesForm

import os

class CoursesListView(ListView):
    """ Выводит список назначенных студенту курсов """
    model = Course
    context_object_name = 'courses'
    paginate_by = 12
    template_name = os.path.join('courses', 'courses_list.html')
    extra_context = {"active_menu": "client", "xxx": "Назначенные курсы"}

    # фильтрация курсов
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(courseandstudents__user_id=self.request.user.pk, courseandstudents__finish_date__lt='1977-01-01')



class CoursesListAllView(ListView):
    """ Выводит список всех курсов """
    model = Course
    context_object_name = 'courses'
    paginate_by = 12
    template_name = os.path.join('courses', 'courses_list.html')
    extra_context = {"active_menu": "client", "xxx": "все курсы"}


class CoursesListCompleteView(ListView):
    """ Выводит список законченных студентом курсов """
    model = Course
    context_object_name = 'courses'
    paginate_by = 12
    template_name = os.path.join('courses', 'courses_list.html')
    extra_context = {"active_menu": "client", "xxx": "выполненые курсы"}


    # фильтрация курсов
    # Исключить  те где дата заверщения меньше 1977 __lt
    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset()
        print(self.request.user.pk)
        return (queryset.filter(courseandstudents__user_id=self.request.user.pk).exclude(courseandstudents__finish_date__lt='1977-01-01'))


class CoursesDetailView(DetailView):
    model = Course
    context_object_name = 'course'
    template_name = os.path.join('courses', 'courses_detail.html')


