# Generated by Django 5.1.1 on 2024-12-15 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_astrobit', '0002_alter_rankuser_player'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamecarddata',
            name='is_active_game',
            field=models.BooleanField(default=False),
        ),
    ]
