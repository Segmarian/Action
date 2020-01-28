from django.db import models


class Skill(models.Model):
    name = models.CharField('Name', max_length=120)


class Proficiency(models.Model):
    class Meta:
        verbose_name_plural="Proficiencies"

    name = models.CharField('Name', max_length=120)


class Attribute(models.Model):
    name = models.CharField('Name', max_length=120)
    start = models.SmallIntegerField()


class Schtick(models.Model):
    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name + "(Tier " + str(self.tier) + ")"

    name = models.CharField('Name', max_length=120)
    req = models.ForeignKey("Attribute", on_delete=models.PROTECT)
    cost = models.CharField(max_length=120)
    description = models.TextField('Description')
    tier = models.PositiveSmallIntegerField()


class Advancement(models.Model):

    def __str__(self):
        return self.name + "(Schtick " + str(self.schtick) + ")"

    schtick = models.ForeignKey(Schtick, on_delete=models.PROTECT)
    name = models.CharField('Name', max_length=120)
    req = models.DateTimeField('Event Date')
    description = models.CharField('Description', max_length=120)
    prereq = models.ForeignKey("Prereq", on_delete=models.PROTECT)


class ValuePair(models.Model):

    def __str__(self):
        return self.name + "(Tier " + str(self.tier) + ")"

    attribute = models.ForeignKey(Attribute, on_delete=models.PROTECT)
    skill = models.ForeignKey(Skill, on_delete=models.PROTECT)
    proficiency = models.ForeignKey(Proficiency, on_delete=models.PROTECT)
    schtick = models.ForeignKey("Schtick", on_delete=models.PROTECT)
    value = models.PositiveSmallIntegerField()


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
