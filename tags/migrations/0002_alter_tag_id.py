# Generated by Django 5.1.6 on 2025-02-26 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='id',
            field=models.CharField(editable=False, max_length=64, primary_key=True, serialize=False),
        ),
    ]
