# Generated by Django 4.1.7 on 2023-02-25 18:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0003_alter_taskhistory_task"),
    ]

    operations = [
        migrations.AlterField(
            model_name="taskhistory",
            name="task",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="tasks.task"
            ),
        ),
    ]
