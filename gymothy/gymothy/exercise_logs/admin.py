from django.contrib import admin

from .models import Exercise, Workout

class ExerciseInLine(admin.StackedInline):
    model = Exercise
    extra = 1

class WorkoutAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["workout_text"]}),
        ("Date information", {"fields": ["workout_date"], "classes": ["collapse"]}),
    ]
    inlines = [ExerciseInLine]

admin.site.register(Workout, WorkoutAdmin)