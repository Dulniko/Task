# Generated by Django 4.1.7 on 2023-02-27 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0004_alter_taskhistory_task"),
    ]

    operations = [
        migrations.AlterField(
            model_name="taskhistory",
            name="task",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="tasks.task"
            ),
        ),
    ]
