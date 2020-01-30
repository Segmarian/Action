# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import ListView, UpdateView

from character.models import *


class CharacterListView (ListView):
    model = Character
    template = "templates/character_list.html"
    fields = '__all__'


class CharacterUpdateView (UpdateView):
    model = Character
    template = "templates/character_detail.html"
    fields = '__all__'
