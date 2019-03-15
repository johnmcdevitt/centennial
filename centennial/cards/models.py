from django.db import models
from random import randint

# Create your models here.

# card - basic item objects
class CardType(models.Model):
    cardtype = models.CharField("Type", max_length=30, unique=True)
    color = models.CharField(max_length=6, unique=True)

    def __str__(self):
        return self.cardtype

    def cardcount(self):
        return Card.objects.filter(type=self).count()

def order_default_value():
    # order will be positive integer, 3 leading digits will be status
    # then a random integer of 6 digits
    max = 100999999
    # min value will be determined by the max value currently in backlog status "100"
    min = Card.objects.filter(status="100").aggregate(models.Max("order"))['order__max']
    if min is None:
        min = 100000000

    return randint(min+1,max-1)

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

    type = models.ForeignKey(CardType, on_delete=models.CASCADE, null=True)
    order = models.PositiveIntegerField(default = order_default_value, unique=True, null=True)


    # metadata fields
    created_date = models.DateField(auto_now_add=True)

    # methods
    def __str__(self):
        return self.title

    def getcolor(self):
        if self.type is None:
            color = '000000'
        else:
            color = self.type.color
        return color
