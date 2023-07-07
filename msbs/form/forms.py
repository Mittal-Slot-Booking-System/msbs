from django import forms
from .models import student,faculty,applicant

class StudentForm(forms.ModelForm):
    class Meta:
        model = student
        fields = '__all__'
class FacultyForm(forms.ModelForm):
    class Meta:
        model = faculty
        fields ='__all__'
