# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from action.models import Attribute, Skill, Flaw, Proficiency, Schtick, ClassEntry, CharacterClass


class Character(models.Model):
    def __str__(self):
        return self.name;

    name = models.CharField('Name', max_length=120)
    points = models.PositiveIntegerField('Points', null=True, blank=True)
    notes = models.TextField('Notes', null=True, blank=True)


class CharacterSchtick(models.Model):
    character = models.ForeignKey(Character, on_delete=models.PROTECT)
    schtick = models.ForeignKey(Schtick, on_delete=models.PROTECT)
    points = models.SmallIntegerField()
    notes = models.CharField('Notes', max_length=120, null=True, blank=True)

    def __str__(self):
        return self.schtick.name + " " + str(self.points)


class CharacterFlaw(models.Model):
    character = models.ForeignKey(Character, on_delete=models.PROTECT)
    flaw = models.ForeignKey(Flaw, on_delete=models.PROTECT)
    points = models.SmallIntegerField()
    notes = models.CharField('Notes', max_length=120, null=True, blank=True)

    def __str__(self):
        return self.flaw.name + " " + str(self.points)


class CharacterAttribute(models.Model):
    character = models.ForeignKey(Character, on_delete=models.PROTECT)
    attribute = models.ForeignKey(Attribute, on_delete=models.PROTECT)
    points = models.SmallIntegerField()
    notes = models.CharField('Notes', max_length=120, null=True, blank=True)

    def __str__(self):
        return self.attribute.name + " " + str(self.points)


class CharacterSkill(models.Model):
    character = models.ForeignKey(Character, on_delete=models.PROTECT)
    skill = models.ForeignKey(Skill, on_delete=models.PROTECT)
    points = models.SmallIntegerField()
    notes = models.CharField('Notes', max_length=120, null=True, blank=True)

    def __str__(self):
        return self.character.name + " " + self.skill.name + " " + str(self.points)


class CharacterProficiency(models.Model):
    class Meta:
        verbose_name_plural = "Character Proficiencies"

    characterskill = models.ForeignKey(CharacterSkill, on_delete=models.PROTECT)
    proficiency = models.ForeignKey(Proficiency, on_delete=models.PROTECT)
    acquired = models.BooleanField()
    notes = models.CharField('Notes', max_length=120, null=True, blank=True)

    def __str__(self):
        return self.characterskill.character.name + " " + self.proficiency.name + " " + str(self.acquired)


class CharacterCharacterClass(models.Model):
    character = models.ForeignKey(Character, on_delete=models.PROTECT)
    characterclass = models.ForeignKey(CharacterClass, on_delete=models.PROTECT)
    level = models.CharField('Level', max_length=120)

    def __str__(self):
        return self.character.name + " " + self.characterclass.name + " " + self.level


class CharacterClassEntry(models.Model):
    character = models.ForeignKey(Character, on_delete=models.PROTECT)
    classentry = models.ForeignKey(ClassEntry, on_delete=models.PROTECT)

    def __str__(self):
        return self.character.name + " " + str(self.classentry)
