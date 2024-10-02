from django import forms
from .models import Employee, Achievement

class EmployeeForm(forms.ModelForm):
    achievements = forms.ModelMultipleChoiceField(
        queryset=Achievement.objects.all(),
        widget=forms.SelectMultiple(attrs={'size': 5}),
        required=False
    )

    class Meta:
        model = Employee
        fields = ['name', 'email', 'phone', 'address', 'department', 'achievements']

    def __init__(self, *args, **kwargs):
        employee_instance = kwargs.pop('employee_instance', None)
        super().__init__(*args, **kwargs)
        self.fields['department'].empty_label = "--SELECT--"
        
        if employee_instance:
            self.fields['achievements'].initial = employee_instance.achievementemployee_set.values_list('achievement_id', flat=True)