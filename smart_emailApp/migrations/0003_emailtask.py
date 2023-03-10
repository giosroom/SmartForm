# Generated by Django 4.1.7 on 2023-03-11 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('smart_emailApp', '0002_remove_emails_subscribe_to_newsletter_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=200)),
                ('task_occurence', models.CharField(blank=True, choices=[('Once', 'Once'), ('Daily', 'Daily'), ('Weekly', 'Weekly'), ('Monthly', 'Monthly')], max_length=50, null=True)),
                ('task_description', models.TextField()),
                ('recipients', models.CharField(max_length=1000)),
                ('sender', models.EmailField(max_length=254)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('date_from', models.DateTimeField()),
                ('date_to_sending', models.DateTimeField()),
                ('status', models.CharField(blank=True, choices=[('Scheduled', 'Scheduled'), ('Not Scheduled', 'Not Scheduled'), ('Expired', 'Expired')], max_length=50, null=True)),
                ('priority', models.CharField(blank=True, choices=[('Scheduled', 'Scheduled'), ('Not Scheduled', 'Not Scheduled'), ('Expired', 'Expired')], max_length=50, null=True)),
                ('error_message', models.TextField(blank=True, null=True)),
                ('email', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='smart_emailApp.emails')),
            ],
        ),
    ]
