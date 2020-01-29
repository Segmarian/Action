# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import *

admin.site.register(Proficiency)
admin.site.register(Attribute)
admin.site.register(Advancement)
admin.site.register(Schtick)
admin.site.register(Flaw)
admin.site.register(Modifier)
admin.site.register(Prereq)
admin.site.register(SchtickType)
admin.site.register(SchtickMod)
admin.site.register(Tag)
