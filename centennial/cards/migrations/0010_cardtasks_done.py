# Generated by Django 2.1.7 on 2019-04-25 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0009_cardtasks'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardtasks',
            name='done',
            field=models.BooleanField(default=False),
        ),
    ]