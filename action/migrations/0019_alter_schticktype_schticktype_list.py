# Generated by Django 3.2.2 on 2021-05-24 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('action', '0018_auto_20210524_0955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schticktype',
            name='schticktype_list',
            field=models.ManyToManyField(blank=True, null=True, related_name='schticktypes', to='action.SchtickType'),
        ),
    ]
