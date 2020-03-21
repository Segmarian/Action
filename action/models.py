from django.db import models


class Skill(models.Model):
    name = models.CharField('Name', max_length=120)
    sortorder = models.SmallIntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


class Proficiency(models.Model):
    class Meta:
        verbose_name_plural = "Proficiencies"

    name = models.CharField('Name', max_length=120)
    skill = models.ForeignKey(Skill, on_delete=models.PROTECT)
    sortorder = models.SmallIntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


class Attribute(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField('Name', max_length=120)
    short_name = models.CharField('Short Name', max_length=10, null=True, blank=True)
    start = models.SmallIntegerField()
    sortorder = models.SmallIntegerField(null=True, blank=True)


class SchtickType(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField('Name', max_length=120)


class Schtick(models.Model):
    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.type.name + ":" + self.name + " (Tier " + str(self.tier) + ")"

    name = models.CharField('Name', max_length=120)
    req = models.ForeignKey("Prereq", on_delete=models.PROTECT,
                            null=True, blank=True, related_name="schtickreq")
    cost = models.CharField("Cost", max_length=120, null=True, blank=True)
    description = models.TextField('Description', null=True, blank=True)
    tier = models.PositiveSmallIntegerField("Tier", null=True, blank=True)
    type = models.ForeignKey("SchtickType", on_delete=models.PROTECT)


class Tag(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField('Name', max_length=120)


class Advancement(models.Model):
    def __str__(self):
        return self.name + "(Schtick " + str(self.schtick) + ")"

    schtick = models.ForeignKey(Schtick, on_delete=models.PROTECT)
    name = models.CharField('Name', max_length=120)
    description = models.CharField('Description', max_length=120,
                                   null=True, blank=True)
    req = models.ForeignKey("Prereq", on_delete=models.PROTECT,
                            null=True, blank=True)


class ValuePair(models.Model):
    def __str__(self):
        return str(self.attribute.name) + \
               str(self.skill.name) + \
               str(self.proficiency.name) + \
               str(self.schtick.name) + " " + \
               str(self.value)

    attribute = models.ForeignKey(Attribute, on_delete=models.PROTECT,
                                  null=True, blank=True, related_name="pv_attribute")
    skill = models.ForeignKey(Skill, on_delete=models.PROTECT,
                              null=True, blank=True, related_name="pv_skill")
    proficiency = models.ForeignKey(Proficiency, on_delete=models.PROTECT,
                                    null=True, blank=True, related_name="pv_proficiency")
    schtick = models.ForeignKey(Schtick, on_delete=models.PROTECT,
                                null=True, blank=True, related_name="pv_schtick")
    value = models.PositiveSmallIntegerField("Value")
    calculated_attribute = models.ForeignKey(Attribute,
                                             on_delete=models.PROTECT,
                                             null=True, blank=True,
                                             related_name="pv_calculated_attribute")


class SchtickMod(ValuePair):
    def __str__(self):
        return self.linked_schtick.name + "mod"

    linked_schtick = models.ForeignKey(Schtick, on_delete=models.PROTECT)
    multiplier = models.BooleanField(blank=True)
    divisor = models.BooleanField(blank=True)


class Flaw(ValuePair):
    name = models.CharField('Name', max_length=120)
    description = models.CharField('Description', max_length=120, blank=True, null=True)

    def __str__(self):
        return str(self.name) + " " + str(self.value)


class Prereq(ValuePair):
    def __str__(self):
        result = ""
        if self.attribute:
            result += self.attribute.name+" "
        if self.skill:
            result += self.skill.name+" "
        if self.proficiency:
            result += self.proficiency.name+" "
        if self.schtick:
            result += self.schtick.name
        return result


class Modifier(ValuePair):
    def __str__(self):
        if self.value < 0:
            sign = "-"
        else:
            sign = "+"
        result=""
        if self.attribute:
            result += self.attribute.name + " "
        if self.skill:
            result += self.skill.name + " "
        if self.proficiency:
            result += self.proficiency.name + " "
        if self.schtick:
            result += self.schtick.name
        return sign + " " + \
            result


class CharacterClass(models.Model):
    class Meta:
        verbose_name_plural = "Character classes"

    def __str__(self):
        return str(self.name)
    name = models.CharField('Name', max_length=120)


class ClassEntry(models.Model):
    class Meta:
        verbose_name_plural = "Class entries"

    def __str__(self):
        schtick = ""
        flaw = ""
        notes = ""
        schtickcost = ""
        flawcost = ""
        if self.notes:
            notes = " " + self.notes
        if self.schtick:
            schtick = str(self.schtick.name)
            schtickcost = str(self.schtick.cost)
        if self.flaw:
            flaw = str(self.flaw.name)
            flawcost = str(self.flaw.value)
        return self.characterclass.name + ":" + \
            self.level + ":" + \
            schtick + flaw + \
            notes + " (" + schtickcost + flawcost + ")"
    characterclass = models.ForeignKey(CharacterClass, on_delete=models.PROTECT)
    level = models.CharField('Level', max_length=120)
    schtick = models.ForeignKey(Schtick, on_delete=models.PROTECT, blank=True, null=True)
    flaw = models.ForeignKey(Flaw, on_delete=models.PROTECT, blank=True, null=True)
    notes = models.CharField('Notes', max_length=120, blank=True, null=True)
