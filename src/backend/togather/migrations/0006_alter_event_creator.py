# Generated by Django 4.2 on 2023-04-17 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('togather', '0005_alter_togatheruser_creator_score_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='creator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='created_events', to='togather.togatheruser'),
        ),
    ]
