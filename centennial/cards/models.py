from django.db import models

# Create your models here.

# card - basic item objects
class Card(models.Model):
    priority_choices = (
        ('3', 'High'),
        ('2', 'Medium'),
        ('1', 'Low'),
    )

    title = models.CharField(max_length=50)
    description = models.CharField(max_length=300, blank=True)
    priority = models.CharField(max_length=1,
                                choices=priority_choices,
                                default='2')

    # metadata fields
    created_date = models.DateField(auto_now_add=True)

    # methods
    def __str__(self):
        return self.title
