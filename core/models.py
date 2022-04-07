import datetime
from django.db import models


class Task(models.Model):

    class Status(models.TextChoices):
        Active = 'Активно'
        Expired = 'Просрочено'
        Completed = 'Завершено'

    StatusBG = {
        Status.Active: 'bg-warning',
        Status.Expired: 'bg-danger',
        Status.Completed: 'bg-success',
    }

    StatusItemBG = {
        Status.Active: '',
        Status.Expired: 'list-group-item-danger',
        Status.Completed: '',
    }

    name = models.CharField('Задача', max_length=500)
    description = models.CharField('Описание', max_length=500, blank=True, null=True)
    data = models.DateField('Последний срок выполнения')
    status = models.CharField('Статус', max_length=500, choices=Status.choices, default=Status.Active, editable=False)

    def __str__(self):
        return self.name

    def get_status_str(self):
        return self.status

    def get_status_bg(self):
        return self.StatusBG[self.status]

    def get_status_item_bg(self):
        return self.StatusItemBG[self.status]

    def get_expired(self):
        return self.data < datetime.date.today()


class Meta:
    verbose_name = 'Задача'
    verbose_name_plural = 'Задачи'
