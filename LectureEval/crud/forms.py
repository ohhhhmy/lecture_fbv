from django import forms
from .models import Lecture, Eval

class EvalForm(forms.ModelForm):
    class Meta:
        model = Eval
        fields = ['title', 'body']
        

class LectureForm(forms.ModelForm):
    class Meta:
        model = Lecture
        fields = ['lectureName', 'professor', 'separation']



