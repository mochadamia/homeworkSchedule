# Generated by Django 2.1.5 on 2019-11-04 06:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homeworkScheduleWeb', '0002_remove_comment_class_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='assignment_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignment', to='homeworkScheduleWeb.Assignment'),
        ),
    ]
