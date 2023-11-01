from django import forms
from .models import Set

WEIGHT_TYPE_CHOICES = [
    ('lb', 'lb'),
    ('kg', 'kg'),
]
    
class SetForm(forms.ModelForm):
    #weights, sets & reps
    weight_num = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Weight'}), required=True)
    weight_type = forms.CharField(widget=forms.Select(choices=WEIGHT_TYPE_CHOICES), required=True)
    set_num = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Set(s)'}), required=True)
    rep_num = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Rep(s)'}), required=True)
    class Meta:
        model = Set
        fields = ('weight_num', 'weight_type', 'set_num', 'rep_num',)