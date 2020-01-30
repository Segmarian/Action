# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import *
# Create your views here.


class CharacterListView (ListView):
    model = Character
    template = "templates/character_list.html"
    fields = '__all__'

class CharacterDetailView (DetailView):
    model = Character
    template = "templates/character_detail.html"
    fields = '__all__'
