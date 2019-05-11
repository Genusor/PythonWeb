from django.db import models

class TodoItem(models.Model):
    description = models.CharField(max_length=64)
    is_completed = models.BooleanField("выполнено", default=False)

    def __str__(self):
        return self.description.lower()
    