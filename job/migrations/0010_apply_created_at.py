# Generated by Django 4.0.5 on 2022-06-20 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0009_apply_jop'),
    ]

    operations = [
        migrations.AddField(
            model_name='apply',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
