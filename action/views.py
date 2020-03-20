# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import ListView, UpdateView, CreateView

from action.models import *


class SchtickListView (ListView):
    model = Schtick
    template_name = "schtick_list.html"
    fields = '__all__'


class SchtickCreateView (CreateView):
    model = Schtick
    template_name = "schtick_detail.html"
    fields = '__all__'


class SchtickUpdateView (UpdateView):
    model = Schtick
    template_name = "schtick_detail.html"
    fields = '__all__'
