# Generated by Django 5.0.3 on 2024-04-04 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('was', '0009_alter_task_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='Score_over',
            field=models.DecimalField(decimal_places=2, default=-1, max_digits=11),
        ),
    ]
