from django.db import models

PRIORITY = (('danger', 'high'), ('info', 'normal'), ('success', 'low'))


class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField()
    priority = models.CharField(
        max_length=50,
        choices=PRIORITY
    )
    duedate = models.DateField()

    def __str__(self):
        return self.title
