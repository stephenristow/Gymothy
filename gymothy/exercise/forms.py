from django import forms
from .models import Exercise

WEIGHT_TYPE_CHOICES = [
    ('lb', 'lb'),
    ('kg', 'kg'),
]
    
class ExerciseForm(forms.ModelForm):
    exercise_text = forms.CharField(widget=forms.TextInput(attrs={"size": "10"}), required=True)

    #weights, sets & reps
    weight_num = forms.IntegerField(widget=forms.NumberInput(), required=True)
    weight_type = forms.CharField(widget=forms.Select(choices=WEIGHT_TYPE_CHOICES), required=True)
    set_num = forms.IntegerField(widget=forms.NumberInput(), required=True)
    rep_num = forms.IntegerField(widget=forms.NumberInput(), required=True)
    class Meta:
        model = Exercise
        fields = ('exercise_text', 'weight_num', 'weight_type', 'set_num', 'rep_num',)