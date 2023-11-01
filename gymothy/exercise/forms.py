from django import forms
from .models import Exercise

WEIGHT_TYPE_CHOICES = [
    ('lb', 'lb'),
    ('kg', 'kg'),
]
    
class ExerciseForm(forms.ModelForm):
    exercise_text = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Exercise',"size": "10"}), required=True)
    class Meta:
        model = Exercise
        fields = ('exercise_text',)