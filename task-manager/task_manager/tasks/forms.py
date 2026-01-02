from django import forms
from django.utils import timezone
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'title',
            'description',
            'due_date',
            'priority',
            'status',
        ]

        widgets = {
            'due_date': forms.DateInput(
                attrs={'type': 'date'}
            ),
        }

    def clean_due_date(self):
        due_date = self.cleaned_data.get('due_date')

        if due_date and due_date < timezone.now().date():
            raise forms.ValidationError(
                "Due date must be in the future."
            )

        return due_date

    def clean_priority(self):
        priority = self.cleaned_data.get('priority')
        valid_priorities = ['Low', 'Medium', 'High']

        if priority not in valid_priorities:
            raise forms.ValidationError(
                "Priority must be Low, Medium, or High."
            )

        return priority

    def clean(self):
        cleaned_data = super().clean()
        status = cleaned_data.get('status')

        if status == 'Completed':
            raise forms.ValidationError(
                "You cannot edit a completed task. Revert it to Pending first."
            )

        return cleaned_data
