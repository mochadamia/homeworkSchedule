# Generated by Django 2.1.5 on 2019-10-28 00:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ClassCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('status', models.CharField(max_length=1)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user_type', models.CharField(default='', max_length=1)),
                ('assignment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homeworkScheduleWeb.Assignment')),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homeworkScheduleWeb.ClassCategory')),
            ],
        ),
        migrations.AddField(
            model_name='assignment',
            name='class_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homeworkScheduleWeb.ClassCategory'),
        ),
    ]