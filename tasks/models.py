from django.db import models

# Create your models here.

class Task(models.Model):
    task_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    due_to = models.CharField(max_length=200)

    def __str__(self):
        return self.task_text


