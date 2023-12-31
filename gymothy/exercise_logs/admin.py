from django.contrib import admin

from .models import Workout, Follow, Stream
from exercise.models import Exercise

class ExerciseInLine(admin.StackedInline):
    model = Exercise
    extra = 1

class WorkoutAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["workout_text"]}),
        ("Date information", {"fields": ["workout_date"], "classes": ["collapse"]}),
        ("User information", {"fields": ["user"]}),
    ]
    inlines = [ExerciseInLine]

admin.site.register(Workout, WorkoutAdmin)
admin.site.register(Follow)
admin.site.register(Stream)