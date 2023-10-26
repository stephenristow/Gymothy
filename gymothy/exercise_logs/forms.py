from django import forms
from .models import Workout

class WorkoutForm(forms.ModelForm):
    workout_text = forms.CharField(widget=forms.TextInput(attrs={"size": "10"}), required=True)

    
    class Meta:
        model = Workout
        fields = ('workout_text',)
    
# class PostExercise(ModelForm):
#     class Meta:
#         model = Exercise
#         fields = "__all__"

# workout_text = models.CharField(max_length=200)
# workout_date = models.DateTimeField("date of workout", default=timezone.now)
# user = models.ForeignKey(User, on_delete=models.CASCADE)