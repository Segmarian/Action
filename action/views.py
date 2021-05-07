# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView

from action.models import *


class CharacterClassListView (ListView):
    model = CharacterClass
    template_name = "action/characterclass_detail.html"
    fields = '__all__'


class CharacterClassUpdateView (UpdateView):
    model = CharacterClass
    template_name = "action/characterclass_detail.html"
    fields = '__all__'
    success_url = reverse_lazy('characterclassupdate')


class CharacterClassCreateView (CreateView):
    model = CharacterClass
    template_name = "action/characterclass_detail.html"
    fields = '__all__'
    success_url = reverse_lazy('characterclassupdate', )


class ClassEntryListView (ListView):
    model = ClassEntry
    template_name = "action/classentry.html"
    fields = '__all__'


class ClassEntryUpdateView (UpdateView):
    model = ClassEntry
    template_name = "action/classentryupdate.html"
    fields = '__all__'


class ClassEntryCreateView (CreateView):
    model = ClassEntry
    template_name = "action/classentrycreate.html"
    fields = '__all__'


class SchtickListView (ListView):
    model = Schtick
    template_name = "action/schtick_list.html"
    fields = '__all__'


class SchtickCreateView (CreateView):
    model = Schtick
    template_name = "action/schtick_detail.html"
    fields = '__all__'


class SchtickUpdateView (UpdateView):
    model = Schtick
    template_name = "action/schtick_detail.html"
    fields = '__all__'


class SchtickTypeUpdateView (UpdateView):
    model = SchtickType
    template_name = "action/schtick_type_detail.html"
    fields = '__all__'


class SchtickTypeCreateView (CreateView):
    model = SchtickType
    template_name = "action/schtick_type_detail.html"
    fields = '__all__'


class PrereqCreateView (CreateView):
    model = Prereq
    template_name = "action/prereq_detail.html"
    fields = '__all__'


class PrereqUpdateView (UpdateView):
    model = Prereq
    template_name = "action/prereq_detail.html"
    fields = '__all__'
