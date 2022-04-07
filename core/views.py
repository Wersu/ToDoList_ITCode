from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, DeleteView, UpdateView

import core.models
import core.forms
from core import models
import datetime


class TitleMixin:
    title: str = None

    def get_title(self):
        return self.title

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = self.get_title()
        return context


class IndexView(TitleMixin, TemplateView):
    template_name = 'core/index.html'
    title = 'Главная страница'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['info'] = self.get_info()
        return context

    def get_info(self):
        return 'Главная страница'


class Tasks(TitleMixin, ListView):
    title = 'Задачи'

    class Meta:
        model = core.models.Task
        fields = ('name',)

    def get_queryset(self):
        name = self.request.GET.get('name')

        for i in core.models.Task.objects.all():
            if i.status == core.models.Task.Status.Active:
                if i.get_expired():
                    i.status = core.models.Task.Status.Expired
                    i.save()

        queryset = core.models.Task.objects.all()
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset

    def get_context_data(self):
        context = super().get_context_data()
        return context


class TaskDetail(TitleMixin, DetailView):
    title = 'Детали задачи'
    queryset = core.models.Task.objects.all()


class TaskUpdate(TitleMixin, UpdateView):
    model = core.models.Task
    form_class = core.forms.TaskEdit

    def get_title(self):
        return f'Изменение задачи "{str(self.get_object())}"'

    def get_success_url(self):
        return reverse('core:task_list')


class TaskCreate(TitleMixin, CreateView):
    model = core.models.Task
    form_class = core.forms.TaskEdit
    title = 'Добавление задачи'

    def get_success_url(self):
        return reverse('core:task_list')


def task_close(request,pk):
    item = core.models.Task.objects.get(pk=pk)
    item.status = core.models.Task.Status.Completed
    item.save()
    return redirect('core:task_list')


class TaskDelete(TitleMixin, DeleteView):
    model = core.models.Task

    def get_title(self):
        return f'Удаление задачи {str(self.get_object())}'

    def get_success_url(self):
        return reverse('core:task_list')
