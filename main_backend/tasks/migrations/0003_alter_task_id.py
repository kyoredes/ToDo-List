# Generated by Django 5.1.6 on 2025-02-26 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_alter_task_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='id',
            field=models.CharField(editable=False, max_length=64, primary_key=True, serialize=False),
        ),
    ]
