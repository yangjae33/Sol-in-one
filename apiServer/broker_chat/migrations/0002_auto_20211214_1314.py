# Generated by Django 3.2.9 on 2021-12-14 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('broker_chat', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='content',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='question_val',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='reliability',
        ),
        migrations.AddField(
            model_name='answer',
            name='accuracy',
            field=models.FloatField(default=-1),
        ),
        migrations.AddField(
            model_name='answer',
            name='answer',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='answer',
            name='chatbot_name',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='answer',
            name='q_idx',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='answer',
            name='chatbot_id',
            field=models.IntegerField(default=-1),
        ),
    ]
