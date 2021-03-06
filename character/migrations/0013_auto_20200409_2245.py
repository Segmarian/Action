# Generated by Django 3.0.3 on 2020-04-09 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('character', '0012_auto_20200331_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charactercharacterclass',
            name='level',
            field=models.CharField(choices=[('Basic', 'Basic'), ('Heroic', 'Heroic'), ('Epic', 'Epic')], max_length=120, verbose_name='Level'),
        ),
        migrations.AlterField(
            model_name='characterproficiency',
            name='acquired',
            field=models.NullBooleanField(blank=True, null=True),
        ),
    ]
