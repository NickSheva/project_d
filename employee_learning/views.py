from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, TemplateView
from employee_learning.models import LearningCourse
from django.urls import reverse_lazy
from django.utils import timezone
# Create your views here.



class CourseList(LoginRequiredMixin, ListView):
    # login_url = "/login/"  # Укажи свой путь к странице логина
    #def get_queryset(self):
        # queryset = LearningCourse.objects.order_by('-title')
        # queryset = LearningCourse.objects.filter(level__contains="B")
        # queryset = LearningCourse.objects.filter(title__endswith="ADVANCED")
    model = LearningCourse
    template_name = 'employee_learning/course_list.html'
    context_object_name = 'course_object_list'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['today'] = timezone.now()
        return context


class CourseDetail(LoginRequiredMixin, DetailView):
    model = LearningCourse
    template_name = 'employee_learning/course_detail.html'
    context_object_name = 'course_object'


class CourseCreate(LoginRequiredMixin, CreateView):
    model = LearningCourse
    template_name = 'employee_learning/course_create.html'
    fields = ('title', 'level', 'employee')
    success_url = reverse_lazy('course_list')

class CourseUpdate(LoginRequiredMixin, UpdateView):
    model = LearningCourse
    template_name = 'employee_learning/course_update.html'
    fields = ('title', 'level', 'employee')
    success_url = reverse_lazy('course_list')


class CourseDelete(LoginRequiredMixin, DeleteView):
    model = LearningCourse
    template_name = 'employee_learning/course_delete.html'
    success_url = reverse_lazy('course_list')


class Index(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['today'] = timezone.now()
        return context