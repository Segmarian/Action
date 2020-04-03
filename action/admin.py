# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from character.models import *
from .models import *


admin.site.register(Skill)
admin.site.register(Proficiency)
admin.site.register(Attribute)
admin.site.register(Advancement)
admin.site.register(Schtick)
admin.site.register(SchtickType)
admin.site.register(Flaw)
admin.site.register(Modifier)
admin.site.register(Prereq)
admin.site.register(SchtickMod)
admin.site.register(Tag)
admin.site.register(CharacterClass)
admin.site.register(ClassEntry)
admin.site.register(Campaign)
admin.site.register(NotInCampaign)
admin.site.register(XPprogression)
