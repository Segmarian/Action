# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from character.models import *

from schtick.models import *
from character.models import *


class SchtickListView (ListView):
    model = Schtick


class SchtickDetailView (DetailView):
    model = Schtick


class CharacterListView (ListView):
    model = Character


class CharacterDetailView (DetailView):
    model = Character
