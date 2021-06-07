# Generated by Django 3.2.2 on 2021-05-24 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('action', '0017_alter_classentry_divisor'),
    ]

    operations = [
        migrations.AddField(
            model_name='schticktype',
            name='schticktype_list',
            field=models.ManyToManyField(related_name='schticktypes', to='action.SchtickType'),
        ),
        migrations.AlterField(
            model_name='classentry',
            name='default',
            field=models.BooleanField(blank=True, null=True, verbose_name='Default'),
        ),
        migrations.AlterField(
            model_name='classentry',
            name='divisor',
            field=models.IntegerField(blank=True, null=True, verbose_name='Divisor'),
        ),
        migrations.AlterField(
            model_name='classentry',
            name='optional',
            field=models.BooleanField(blank=True, null=True, verbose_name='Optional'),
        ),
    ]