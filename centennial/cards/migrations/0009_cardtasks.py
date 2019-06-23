# Generated by Django 2.1.7 on 2019-04-24 23:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0008_cardtype_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='CardTasks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.TextField(help_text='What do you need to do')),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cards.Card')),
            ],
        ),
    ]
