from django.db import models

class Application(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(
        max_length=20,
        choices=[
            ('Running', 'Running'),
            ('Error', 'Error'),
            ('Stopped', 'Stopped'),
        ]
    )

    def __str__(self):
        return self.name
