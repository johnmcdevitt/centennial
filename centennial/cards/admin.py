from django.contrib import admin

# Register your models here.
from .models import Card, CardType, CardTask

admin.site.register([Card, CardType, CardTask])
