# Generated by Django 2.2.3 on 2019-09-21 06:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_auto_20190921_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='due_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
