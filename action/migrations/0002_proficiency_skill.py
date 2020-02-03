# Generated by Django 3.0.2 on 2020-02-02 01:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('action', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='proficiency',
            name='skill',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='action.Skill'),
            preserve_default=False,
        ),
    ]
