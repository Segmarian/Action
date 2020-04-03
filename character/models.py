# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models import IntegerField

from action.models import Attribute, Skill, Flaw, Proficiency, Schtick, ClassEntry, \
    CharacterClass, Advancement


class CharacterSchtick(models.Model):
    character = models.ForeignKey('Character', on_delete=models.PROTECT)
    schtick = models.ForeignKey(Schtick, on_delete=models.PROTECT)
    points = models.PositiveSmallIntegerField()
    notes = models.CharField('Notes', max_length=120, null=True, blank=True)

    def __str__(self):
        return self.schtick.name + " " + str(self.points)


class CharacterFlaw(models.Model):
    character = models.ForeignKey('Character', on_delete=models.PROTECT)
    flaw = models.ForeignKey(Flaw, on_delete=models.PROTECT)
    points = models.SmallIntegerField()
    notes = models.CharField('Notes', max_length=120, null=True, blank=True)

    def __str__(self):
        return self.flaw.name + " " + str(self.points)


class CharacterAttribute(models.Model):
    character = models.ForeignKey('Character', on_delete=models.PROTECT)
    attribute = models.ForeignKey(Attribute, on_delete=models.PROTECT)
    points = models.SmallIntegerField()
    notes = models.CharField('Notes', max_length=120, null=True, blank=True)

    def __str__(self):
        return self.character.name + ":" + self.attribute.name + " " + str(self.points)


class CharacterSkill(models.Model):
    character = models.ForeignKey('Character', on_delete=models.PROTECT)
    skill = models.ForeignKey(Skill, on_delete=models.PROTECT)
    points = models.PositiveSmallIntegerField()
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
    character = models.ForeignKey('Character', on_delete=models.PROTECT)
    characterclass = models.ForeignKey(CharacterClass, on_delete=models.PROTECT)
    
    level = models.CharField('Level', max_length=120, choices={('Basic', 'Basic'),('Heroic', 'Heroic'),('Epic', 'Epic')})

    def __str__(self):
        return self.character.name + " " + self.characterclass.name + " " + self.level


class CharacterClassEntry(models.Model):
    character_characterclass = models.ForeignKey(CharacterCharacterClass, on_delete=models.PROTECT)
    classentry = models.ForeignKey(ClassEntry, on_delete=models.PROTECT)
    notes = models.CharField('Notes', max_length=120, null=True, blank=True)
    points = models.SmallIntegerField()

    def __str__(self):
        return str(self.character_characterclass) + " " + str(self.classentry)


class CharacterAdvancement(models.Model):
    characterschtick = models.ForeignKey(CharacterSchtick, on_delete=models.PROTECT)
    advancement = models.ForeignKey(Advancement, on_delete=models.PROTECT)
    notes = models.CharField('Notes', max_length=120, null=True, blank=True)
    points = models.SmallIntegerField()


class Character(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField('Name', max_length=120)
    points = models.PositiveIntegerField('Points', null=True, blank=True)
    notes = models.TextField('Notes', null=True, blank=True)

    @property
    def xp(self):
        attrset = CharacterAttribute.objects.filter(character=self)
        attrxp = attrset.aggregate(models.Sum('points'))['points__sum'] or 0
        attrxp = attrxp - (attrset.count() or 0)*5
        charskills = CharacterSkill.objects.filter(character=self)
        skillxp = (charskills.aggregate(models.Sum('points'))['points__sum'] or 0) - (charskills.count() or 0)*10
        profxp = CharacterProficiency.objects.filter(characterskill__in=charskills, acquired=True).count()
        charschticks = CharacterSchtick.objects.filter(character=self)
        schtickxp = charschticks.aggregate(models.Sum('points'))['points__sum'] or 0
        advxp = CharacterAdvancement.objects.filter(characterschtick__in=charschticks)\
            .aggregate(models.Sum('points'))['points__sum'] or 0
        charclass = CharacterCharacterClass.objects.filter(character=self)
        classxp = CharacterClassEntry.objects.filter(character_characterclass__in=charclass)\
            .aggregate(models.Sum('classentry__schtick__cost'))['classentry__schtick__cost__sum'] or 0
        flawxp = CharacterFlaw.objects.filter(character=self).aggregate(models.Sum('points'))['points__sum'] or 0
        xp = {'attribute': attrxp,
              'skill': skillxp+profxp,
              'schtick': schtickxp + advxp,
              'class': classxp,
              'flaw': flawxp,
              'total': attrxp + skillxp + profxp + schtickxp + advxp + classxp - flawxp
              }
        return xp
