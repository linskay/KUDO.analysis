from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from ..models import Course, CourseAndStudents, User
from django.views.generic import ListView, DetailView
from ..forms import CoursesForm

import os

class CoursesListView(ListView):
    model = Course
    context_object_name = 'courses'
    paginate_by = 12
    template_name = os.path.join('courses', 'courses_list.html')
    extra_context = {"active_menu": "client", "xxx": "Назначенные курсы"}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = Course.objects.filter(courseandstudents__user_id=self.request.user.pk).exclude(courseandstudents__finish_date=None)
        return context


class CoursesListAllView(ListView):
    model = Course
    context_object_name = 'courses'
    paginate_by = 12
    template_name = os.path.join('courses', 'courses_list.html')
    extra_context = {"active_menu": "client", "xxx": "все курсы"}


class CoursesListCompleteView(ListView):
    model = Course
    context_object_name = 'courses'
    paginate_by = 12
    template_name = os.path.join('courses', 'courses_list.html')
    extra_context = {"active_menu": "client", "xxx": "выполненые курсы"}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = Course.objects.filter(courseandstudents__user_id=self.request.user.pk, courseandstudents__finish_date=None)
        return context

class CoursesDetailView(DetailView):
    model = Course
    context_object_name = 'course'
    template_name = os.path.join('courses', 'courses_detail.html')
    #extra_context = {"active_menu": "client"}


class CoursesUpdateView(UpdateView):
    model = Course
    form_class = CoursesForm
    #fields = ['name_course', 'description_course', 'photo_course', 'pay_course', 'students']
    context_object_name = 'course'
    template_name = os.path.join('courses', 'courses_form.html')
    success_url = reverse_lazy('courses:courses')
    #extra_context = {"active_menu": "client"}

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.path_img_temp = None
        self.photo_course_old = None
        if self.object.photo_course:
            # сохраняю путь к старому фото
            self.path_img_temp = self.object.photo_course.path
            self.photo_course_old = self.object.photo_course

        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        # Удалить файл картинки
        if self.photo_course_old:
            if self.photo_course_old != self.object.photo_course:
                os.remove(self.path_img_temp)

        #if (not self.object.photo_course and self.path_img_temp) or (self.object.photo_course_old != self.object.photo_course):
           # os.remove(self.path_img_temp)
        return super().form_valid(form)


class CoursesCreateView(CreateView):
    model = Course
    form_class = CoursesForm
    #fields = ['name_course','description_course','photo_course','pay_course','students']
    context_object_name = 'course'
    template_name = os.path.join('courses', 'courses_form.html')
    success_url = reverse_lazy('courses:courses')
    # extra_context = {"active_menu": "client"}

class CoursesDeleteView(DeleteView):
    model = Course
    context_object_name = 'course'
    success_url = reverse_lazy('courses:courses')
    template_name = os.path.join('courses', 'courses_delete.html')
    extra_context = {"active_menu": "client"}

    def form_valid(self, form):
        # Удалить файл картинки
        if self.object.photo_course:
            path = self.object.photo_course.path
            os.remove(path)
        return super().form_valid(form)
