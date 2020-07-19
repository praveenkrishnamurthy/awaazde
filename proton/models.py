from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    duration = models.DurationField()
    last_edited = models.DateTimeField()

    def __str__(self):
        return self.name


class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name

