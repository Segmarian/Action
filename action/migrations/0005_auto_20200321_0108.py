# Generated by Django 3.0.3 on 2020-03-21 00:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('action', '0004_auto_20200320_2114'),
    ]

    operations = [
        migrations.CreateModel(
            name='CharacterClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Name')),
            ],
        ),
        migrations.AlterField(
            model_name='schtickmod',
            name='divisor',
            field=models.BooleanField(blank=True),
        ),
        migrations.AlterField(
            model_name='schtickmod',
            name='multiplier',
            field=models.BooleanField(blank=True),
        ),
        migrations.CreateModel(
            name='ClassEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(max_length=120, verbose_name='Level')),
                ('notes', models.CharField(blank=True, max_length=120, null=True, verbose_name='Notes')),
                ('characterclass', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='action.CharacterClass')),
                ('schtick', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='action.Schtick')),
            ],
        ),
    ]