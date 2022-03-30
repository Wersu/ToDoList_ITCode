from django.shortcuts import render
import core.models


def index(request):
    tasks = core.models.Task.objects.all()
    return render(request, 'core/index.html', {'objects_list': tasks})
