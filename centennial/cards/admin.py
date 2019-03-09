from django.contrib import admin

# Register your models here.
from .models import Card, CardType

admin.site.register([Card, CardType])
