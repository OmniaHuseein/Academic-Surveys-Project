from django import forms

from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = (
            'secondary_email',
            'status',
            'educational_year',
            'academic_year',
            'department',
            'courses',
        )
