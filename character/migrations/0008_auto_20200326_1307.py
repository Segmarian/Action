# Generated by Django 3.0.3 on 2020-03-26 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('character', '0007_characterclassentry_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charactercharacterclass',
            name='level',
            field=models.CharField(choices=[('Epic', 'Epic'), ('Basic', 'Basic'), ('Heroic', 'Heroic')], max_length=120, verbose_name='Level'),
        ),
        migrations.AlterField(
            model_name='characterclassentry',
            name='notes',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='Notes'),
        ),
    ]