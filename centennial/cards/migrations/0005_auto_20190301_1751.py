# Generated by Django 2.1.5 on 2019-03-01 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0004_card_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='order',
            field=models.BigIntegerField(null=True, unique=True),
        ),
    ]
