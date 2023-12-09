from django import forms
from .models import Set
from exercise.models import Exercise

WEIGHT_TYPE_CHOICES = [
    ('lb', 'lb'),
    ('kg', 'kg'),
]
    
class SetForm(forms.ModelForm):
    #weights, sets & reps
    weight_num = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Weight'}), required=True)
    weight_type = forms.CharField(widget=forms.Select(choices=WEIGHT_TYPE_CHOICES), required=True)
    rep_num = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Rep(s)'}), required=True)

    #exercise
    exercise_id = forms.IntegerField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Set
        fields = ('weight_num', 'weight_type', 'rep_num', 'exercise_id')