from django.db import models


class Skill(models.Model):
    name = models.CharField('Name', max_length=120)


class Proficiency(models.Model):
    class Meta:
        verbose_name_plural="Proficiencies"

    name = models.CharField('Name', max_length=120)


class Attribute(models.Model):

    def __str__(self):
        return self.name + " (" + str(self.start)+ ")"

    name = models.CharField('Name', max_length=120)
    short_name = models.CharField('Short Name', max_length=10, null=True, blank=True)
    start = models.SmallIntegerField()


class Schtick(models.Model):
    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name + "(Tier " + str(self.tier) + ")"

    name = models.CharField('Name', max_length=120)
    prereq = models.ForeignKey("Prereq", on_delete=models.PROTECT, null=True, blank=True)
    cost = models.CharField("Cost", max_length=120, null=True, blank=True)
    description = models.TextField('Description', null=True, blank=True)
    tier = models.PositiveSmallIntegerField("Tier", null=True, blank=True)


class Advancement(models.Model):

    def __str__(self):
        return self.name + "(Schtick " + str(self.schtick) + ")"

    schtick = models.ForeignKey(Schtick, on_delete=models.PROTECT)
    name = models.CharField('Name', max_length=120)
    description = models.CharField('Description', max_length=120, null=True, blank=True)
    prereq = models.ForeignKey("Prereq", on_delete=models.PROTECT, null=True, blank=True)


class ValuePair(models.Model):

    def __str__(self):
        return self.name + "(Tier " + str(self.tier) + ")"

    attribute = models.ForeignKey(Attribute, on_delete=models.PROTECT, null=True, blank=True)
    skill = models.ForeignKey(Skill, on_delete=models.PROTECT, null=True, blank=True)
    proficiency = models.ForeignKey(Proficiency, on_delete=models.PROTECT, null=True, blank=True)
    schtick = models.ForeignKey("Schtick", on_delete=models.PROTECT, null=True, blank=True)
    value = models.PositiveSmallIntegerField("Value")


class Flaw(ValuePair):
    name = models.CharField('Name', max_length=120)

    def __str__(self):
        return self.name + " " + str(self.value)


class Prereq(ValuePair):
    def __str__(self):
        return self.attribute.name + \
               self.skill.name + \
               self.proficiency.name + \
               self.schtick + " " + \
               str(self.value)


class Modifier(ValuePair):
    def __str__(self):
        if self.value < 0:
            sign="-"
        else:
            sign="+"
        return self.sign + " "+ \
            str(self.value) + " " + \
            self.attribute.name + \
            self.skill.name + \
            self.proficiency.name + \
            self.schtick
