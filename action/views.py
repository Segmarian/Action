# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import ListView, UpdateView, CreateView, TemplateView
from django.urls import reverse_lazy
from django_filters.views import FilterView

from action.filters import *
from action.models import *


class ActionView (TemplateView):
    template_name = "action/index.html"


class CharacterClassListView (FilterView):
    model = CharacterClass
    template_name = "action/characterclass_list.html"
    fields = '__all__'
    filterset_class = CharClassFilter


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


class ClassEntryListView (FilterView):
    model = ClassEntry
    template_name = "action/classentry.html"
    fields = '__all__'
    filterset_class = ClassEntryFilter


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


class SchtickListView (FilterView):
    model = Schtick
    template_name = "action/schtick_list.html"
    fields = '__all__'
    filterset_class = SchtickFilter


class SchtickCreateView (CreateView):
    model = Schtick
    template_name = "action/schtick_detail.html"
    fields = '__all__'
    success_url = reverse_lazy('schticks', )


class SchtickUpdateView (UpdateView):
    model = Schtick
    template_name = "action/schtick_detail.html"
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('schtick_detail', kwargs={"pk": self.object.pk})


class FlawListView (FilterView):
    model = Flaw
    template_name = "action/flaw_list.html"
    fields = '__all__'
    filterset_class = FlawFilter


class FlawCreateView (CreateView):
    model = Flaw
    template_name = "action/flaw_detail.html"
    fields = '__all__'
    success_url = reverse_lazy('flaws', )


class FlawUpdateView (UpdateView):
    model = Flaw
    template_name = "action/flaw_detail.html"
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('flaw_detail', kwargs={"pk": self.object.pk})


class SchtickTypeListView (FilterView):
    model = SchtickType
    template_name = "action/schticktype_list.html"
    fields = '__all__'
    filterset_class = SchtickTypeFilter


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
    success_url = reverse_lazy('schticktypes', )


class SchtickTypeCreateReturnView (CreateView):
    model = SchtickType
    template_name = "action/schticktype_detail.html"
    fields = '__all__'
    success_url = reverse_lazy('charclass_create', )


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


class CampaignListView (ListView):
    model = Campaign
    template_name = "action/campaign_list.html"
    fields = '__all__'


class CampaignCreateView (CreateView):
    model = Campaign
    template_name = "action/campaign_detail.html"
    fields = '__all__'
    success_url = reverse_lazy('campaigns')


class CampaignUpdateView (UpdateView):
    model = Campaign
    template_name = "action/campaign_detail.html"
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('campaign_detail', kwargs={"pk": self.object.pk})

def product_list(request):
    f = ProductFilter(request.GET, queryset=Product.objects.all())
    return render(request, 'my_app/template.html', {'filter': f})