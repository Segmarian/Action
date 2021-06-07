# Generated by Django 3.2.2 on 2021-05-18 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('character', '0017_alter_charactercharacterclass_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charactercharacterclass',
            name='level',
            field=models.CharField(choices=[('Epic', 'Epic'), ('Basic', 'Basic'), ('Heroic', 'Heroic')], max_length=120, verbose_name='Level'),
        ),
        migrations.AlterField(
            model_name='characterproficiency',
            name='acquired',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]