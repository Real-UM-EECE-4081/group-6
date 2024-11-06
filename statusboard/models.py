from django.db import models

# Create your models here.
class Application(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=[('Running', 'Running'), ('Error', 'Error')])

    def __str__(self):
        return self.name

class Incident(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE, related_name='incidents')
    description = models.TextField()
    occurred_at = models.DateTimeField(auto_now_add=True)
    resolved = models.BooleanField(default=False)

    def __str__(self):
        return f"Incident for {self.application.name} at {self.occurred_at}"
