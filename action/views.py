# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, TemplateView

from action.models import *


class ActionView (TemplateView):
    template_name = "action/index.html"


class CharacterClassListView (ListView):
    model = CharacterClass
    template_name = "action/characterclass_list.html"
    fields = '__all__'


class CharacterClassUpdateView (UpdateView):
    model = CharacterClass
    template_name = "action/characterclass_detail.html"
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('characterclass_detail', kwargs={'pk': self.object.pk})


class CharacterClassCreateView (CreateView):
    model = CharacterClass
    template_name = "action/characterclass_detail.html"
    fields = '__all__'
    success_url = reverse_lazy('characterclass_list', )


class ClassEntryListView (ListView):
    model = ClassEntry
    template_name = "action/classentry.html"
    fields = '__all__'


class ClassEntryUpdateView (UpdateView):
    model = ClassEntry
    template_name = "action/classentryupdate.html"
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('classentry_detail', kwargs={'pk': self.object.pk})


class ClassEntryCreateView (CreateView):
    model = ClassEntry
    template_name = "action/classentrycreate.html"
    fields = '__all__'
    success_url = reverse_lazy('classentry_list', )


class SchtickListView (ListView):
    model = Schtick
    template_name = "action/schtick_list.html"
    fields = '__all__'


class SchtickCreateView (CreateView):
    model = Schtick
    template_name = "action/schtick_detail.html"
    fields = '__all__'
    success_url = reverse_lazy('schtick_detail', )


class SchtickUpdateView (UpdateView):
    model = Schtick
    template_name = "action/schtick_detail.html"
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('schtick_detail', kwargs={"pk": self.object.pk})


class SchtickTypeListView (ListView):
    model = SchtickType
    template_name = "action/schticktype_list.html"
    fields = '__all__'


class SchtickTypeUpdateView (UpdateView):
    model = SchtickType
    template_name = "action/schticktype_detail.html"
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('schticktype_detail', kwargs={"pk": self.object.pk})


class SchtickTypeCreateView (CreateView):
    model = SchtickType
    template_name = "action/schticktype_detail.html"
    fields = '__all__'
    success_url = reverse_lazy('schticktype_list', )


class PrereqListView (ListView):
    model = Prereq
    template_name = "action/prereq_list.html"
    fields = '__all__'


class PrereqCreateView (CreateView):
    model = Prereq
    template_name = "action/prereq_detail.html"
    fields = '__all__'
    success_url = reverse_lazy('prereqs')


class PrereqUpdateView (UpdateView):
    model = Prereq
    template_name = "action/prereq_detail.html"
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('prereq_detail', kwargs={"pk": self.object.pk})
