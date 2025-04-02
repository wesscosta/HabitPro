from django.conf import settings
from django.db import models
from django.utils.timezone import now

class Habit(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='habits')
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    location = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.title} (criado em {self.created_at})"

class CheckIn(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE, related_name='check_ins')
    check_in_time = models.DateTimeField(default=now)
    location = models.CharField(max_length=255, blank=True, null=True)
    status = models.BooleanField(default=False)  # Concluído ou não
    
    def __str__(self):
        return f"{self.habit.title} ➔ check-in {self.check_in_time} ({self.status})"
