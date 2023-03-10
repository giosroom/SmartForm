# Generated by Django 4.1.7 on 2023-03-11 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smart_formApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='welcome_email',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='subscribe_to_newsletter',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
