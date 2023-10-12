from django import forms
from .models import Exercise


    
class ExerciseForm(forms.ModelForm):
    exercise_text = forms.CharField(widget=forms.Textarea(attrs={'class': 'input is-medium'}), required=True)

    #weights, sets & reps
    weight_num = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'input is-medium'}), required=True)
    weight_type = forms.CharField(widget=forms.Textarea(attrs={'class': 'input is-medium'}), required=True)
    set_num = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'input is-medium'}), required=True)
    rep_num = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'input is-medium'}), required=True)
    class Meta:
        model = Exercise
        fields = ('exercise_text', 'weight_num', 'weight_type', 'set_num', 'rep_num',)