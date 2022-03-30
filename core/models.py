from django.db import models


class Task(models.Model):
    name = models.CharField('Задача', max_length=500)
    description = models.CharField('Описание', max_length=500)

    def __str__(self):
        return self.name
