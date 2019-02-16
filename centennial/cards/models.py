from django.db import models

# Create your models here.

# card - basic item objects
class Card(models.Model):
    priority_choices = (
        ('3', 'High'),
        ('2', 'Medium'),
        ('1', 'Low'),
    )
    status_choices = (
        ('100', 'Backlog'),
        ('200', 'To do'),
        ('300', 'In progress'),
        ('400', 'Review'),
        ('500', 'Done'),
    )

    title = models.CharField(max_length=50)
    description = models.CharField(max_length=300, blank=True)
    priority = models.CharField(max_length=1,
                                choices=priority_choices,
                                default='2')
    status = models.CharField(max_length=3,
                                choices=status_choices,
                                default='100')

    # metadata fields
    created_date = models.DateField(auto_now_add=True)

    # methods
    def __str__(self):
        return self.title
