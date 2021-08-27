# Generated by Django 3.2.6 on 2021-08-27 15:52

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('session_id', models.UUIDField()),
                ('category', models.CharField(max_length=40)),
                ('name', models.CharField(max_length=40)),
                ('data', models.JSONField()),
                ('timestamp', models.DateTimeField()),
            ],
        ),
    ]