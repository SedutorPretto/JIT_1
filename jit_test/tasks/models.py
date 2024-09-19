from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название', blank=False, null=False)
    description = models.TextField(blank=True, verbose_name='Описание')
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
