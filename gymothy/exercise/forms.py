from django import forms
from .models import Exercise

WEIGHT_TYPE_CHOICES = [
    ('lb', 'lb'),
    ('kg', 'kg'),
]
    
class ExerciseForm(forms.ModelForm):
    exercise_text = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Exercise',"size": "10"}), required=True)

    #weights, sets & reps
    weight_num = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Weight'}), required=True)
    weight_type = forms.CharField(widget=forms.Select(choices=WEIGHT_TYPE_CHOICES), required=True)
    set_num = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Set(s)'}), required=True)
    rep_num = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Rep(s)'}), required=True)
    class Meta:
        model = Exercise
        fields = ('exercise_text', 'weight_num', 'weight_type', 'set_num', 'rep_num',)