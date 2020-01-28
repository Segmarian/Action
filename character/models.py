# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from action.models import Attribute, Skill, Flaw, Proficiency, Schtick


class Character(models.Model):
    name = models.CharField('Name', max_length=120)


class CharacterMixin(models.Model):
    character = models.ForeignKey(Character, on_delete=models.PROTECT)


class CharacterSchtick(CharacterMixin, models.Model):
    schtick = models.ForeignKey(Schtick, on_delete=models.PROTECT)
    points = models.SmallIntegerField()


class CharacterFlaw(CharacterMixin, models.Model):
    flaw = models.ForeignKey(Flaw, on_delete=models.PROTECT)
    points = models.SmallIntegerField()


class CharacterAttribute(CharacterMixin, models.Model):
    attribute = models.ForeignKey(Attribute, on_delete=models.PROTECT)
    points = models.SmallIntegerField()


class CharacterSkill(CharacterMixin, models.Model):
    skill = models.ForeignKey(Skill, on_delete=models.PROTECT)
    points = models.SmallIntegerField()


class CharacterProficiency(CharacterMixin, models.Model):
    class Meta:
        verbose_name_plural = "Proficiencies"

    proficiency = models.ForeignKey(Proficiency, on_delete=models.PROTECT)
    acquired = models.SmallIntegerField()
