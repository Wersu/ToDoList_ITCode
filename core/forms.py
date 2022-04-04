from django import forms
import core.models


class TaskEdit(forms.ModelForm):
    class Meta:
        model = core.models.Task
        fields = '__all__'


