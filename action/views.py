# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from character.models import *

from schtick.models import *


class SchtickListView (ListView):
    model = Schtick
    template_name = "templates/schtick_list.html"
    fields = '__all__'

class SchtickDetailView (DetailView):
    model = Schtick
    template_name = "templates/schtick_detail.html"
    fields = '__all__'
