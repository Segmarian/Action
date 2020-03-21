# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import *

admin.site.register(Character)
admin.site.register(CharacterAttribute)
admin.site.register(CharacterFlaw)
admin.site.register(CharacterProficiency)
admin.site.register(CharacterSchtick)
admin.site.register(CharacterSkill)
admin.site.register(CharacterCharacterClass)
admin.site.register(CharacterClassEntry)