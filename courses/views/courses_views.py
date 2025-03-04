from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from ..models import Course
from django.views.generic import ListView, DetailView

import os

class CoursesListView(ListView):
    model = Course
    context_object_name = 'courses'
    paginate_by = 12
    template_name = os.path.join('courses', 'courses_list.html')
    extra_context = {"active_menu": "client"}


class CoursesDetailView(DetailView):
    model = Course
    context_object_name = 'course'
    template_name = os.path.join('courses', 'courses_detail.html')
    #extra_context = {"active_menu": "client"}


class CoursesUpdateView(UpdateView):
    model = Course
    #form_class = CourseForm\
    fields = ['name_course', 'description_course', 'photo_course', 'pay_course', 'students']
    context_object_name = 'course'
    template_name = os.path.join('courses', 'courses_form.html')
    success_url = reverse_lazy('courses:courses')
    #extra_context = {"active_menu": "client"}


class CoursesCreateView(CreateView):
    model = Course
    # form_class = CourseForm\
    fields = ['name_course','description_course','photo_course','pay_course','students']
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
