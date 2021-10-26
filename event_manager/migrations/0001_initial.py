# Generated by Django 3.2.6 on 2021-10-18 20:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('idea_manager', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('ideas', models.ManyToManyField(related_name='events', to='idea_manager.DateIdea')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_owner', to=settings.AUTH_USER_MODEL)),
                ('participants', models.ManyToManyField(related_name='event_participants', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
