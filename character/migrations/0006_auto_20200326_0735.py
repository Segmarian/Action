# Generated by Django 3.0.3 on 2020-03-26 06:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('character', '0005_auto_20200321_0108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='characterclassentry',
            name='character',
        ),
        migrations.AddField(
            model_name='characterclassentry',
            name='character_characterclass',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='character.CharacterCharacterClass'),
            preserve_default=False,
        ),
    ]
