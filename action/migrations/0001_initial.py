# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2020-01-28 23:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advancement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name=b'Name')),
                ('req', models.DateTimeField(verbose_name=b'Event Date')),
                ('description', models.CharField(max_length=120, verbose_name=b'Description')),
            ],
        ),
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name=b'Name')),
                ('start', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Proficiency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name=b'Name')),
            ],
            options={
                'verbose_name_plural': 'Proficiencies',
            },
        ),
        migrations.CreateModel(
            name='Schtick',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name=b'Name')),
                ('cost', models.CharField(max_length=120)),
                ('description', models.TextField(verbose_name=b'Description')),
                ('tier', models.PositiveSmallIntegerField()),
                ('req', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='action.Attribute')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name=b'Name')),
            ],
        ),
        migrations.CreateModel(
            name='ValuePair',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Flaw',
            fields=[
                ('valuepair_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='action.ValuePair')),
                ('name', models.CharField(max_length=120, verbose_name=b'Name')),
            ],
            bases=('action.valuepair',),
        ),
        migrations.CreateModel(
            name='Modifier',
            fields=[
                ('valuepair_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='action.ValuePair')),
            ],
            bases=('action.valuepair',),
        ),
        migrations.CreateModel(
            name='Prereq',
            fields=[
                ('valuepair_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='action.ValuePair')),
            ],
            bases=('action.valuepair',),
        ),
        migrations.AddField(
            model_name='valuepair',
            name='attribute',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='action.Attribute'),
        ),
        migrations.AddField(
            model_name='valuepair',
            name='proficiency',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='action.Proficiency'),
        ),
        migrations.AddField(
            model_name='valuepair',
            name='schtick',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='action.Schtick'),
        ),
        migrations.AddField(
            model_name='valuepair',
            name='skill',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='action.Skill'),
        ),
        migrations.AddField(
            model_name='advancement',
            name='schtick',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='action.Schtick'),
        ),
        migrations.AddField(
            model_name='advancement',
            name='prereq',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='action.Prereq'),
        ),
    ]
