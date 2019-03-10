# Generated by Django 2.1.5 on 2019-03-04 01:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('house', '0003_room'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='uploads/images/')),
                ('image_type', models.CharField(choices=[('b', 'Before'), ('i', 'Inspiration'), ('a', 'After'), ('p', 'To Do')], max_length=1)),
                ('room', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='house.Room')),
            ],
        ),
    ]
