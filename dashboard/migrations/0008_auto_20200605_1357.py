# Generated by Django 3.0.6 on 2020-06-05 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_messages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='message_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]