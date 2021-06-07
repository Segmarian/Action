from django.contrib import admin
from django.conf.urls import url
from action.views import *
from character.views import *


class CharacterDeleteView (DeleteView):
    pass


class CharacterClassDeleteView(DeleteView):
    pass


urlpatterns = [
    url(r'admin/', admin.site.urls),

    url(r'^campaign/(?P<pk>[0-9]+)/', CampaignUpdateView.as_view(), name="campaign_detail"),
    url(r'^campaign/new/', CampaignCreateView.as_view(), name="campaign_create"),
    url(r'^campaign/', CampaignListView.as_view(), name="campaigns"),

    url(r'^character/(?P<pk>[0-9]+)/attribute/', CharacterAttributeView.as_view(),
         name="characterattribute"),
    url(r'^character/(?P<pk>[0-9]+)/flaw/', CharacterFlawView.as_view(), name="character_flaw"),
    url(r'^character/(?P<pk>[0-9]+)/schtick/', CharacterSchtickView.as_view(), name="character_schtick"),
    url(r'^character/(?P<pk>[0-9]+)/basic/', CharacterBasicView.as_view(), name="character_basic"),

    url(r'^character/delete/(?P<pk>[0-9]+)/', CharacterDeleteView.as_view(), name='characterclass_delete'),
    url(r'^character/(?P<pk>[0-9]+)/', CharacterDetailView.as_view(), name="character_detail"),
    url(r'^character/new/', CharacterCreateView.as_view(), name="character_create"),
    url(r'^character/', CharacterListView.as_view(), name="characters"),

    url(r'^charclass/delete/(?P<pk>[0-9]+)/', CharacterClassDeleteView.as_view(), name='characterclass_delete'),
    url(r'^charclass/(?P<pk>[0-9]+)/', CharacterClassUpdateView.as_view(), name='characterclass_detail'),
    url(r'^charclass/new/', CharacterClassCreateView.as_view(), name='characterclass_create'),
    url(r'^charclass/entry/(?P<pk>[0-9]+)/', ClassEntryUpdateView.as_view(), name='classentry_detail'),
    url(r'^charclass/entry/new/(?P<item>[0-9]+)/', ClassEntryCreateFromClassView.as_view(), name='classentry_create_from_class'),
    url(r'^charclass/entry/new/', ClassEntryCreateView.as_view(), name='classentry_create'),
    url(r'^charclass/entry/', ClassEntryListView.as_view(), name='classentry_list'),
    url(r'^charclass/', CharacterClassListView.as_view(), name='characterclass_list'),

    url(r'^schtick/type/delete/(?P<pk>[0-9]+)/', SchtickTypeDeleteView.as_view(), name="schticktype_delete"),
    url(r'^schtick/type/(?P<pk>[0-9]+)/', SchtickTypeUpdateView.as_view(), name="schticktype_detail"),
    url(r'^schtick/type/new/', SchtickTypeCreateView.as_view(), name="schticktype_create"),
    url(r'^schtick/type/new/return/', SchtickTypeCreateReturnView.as_view(), name="schticktype_return_create"),
    url(r'^schtick/type/', SchtickTypeListView.as_view(), name="schticktypes"),

    url(r'^schtick/delete/(?P<pk>[0-9]+)/', SchtickDeleteView.as_view(), name="schtick_delete"),
    url(r'^schtick/(?P<pk>[0-9]+)/', SchtickUpdateView.as_view(), name="schtick_detail"),
    url(r'^schtick/new/', SchtickCreateView.as_view(), name="schtick_create"),
    url(r'^schtick/', SchtickListView.as_view(), name="schticks"),

    url(r'^flaw/delete/(?P<pk>[0-9]+)/', PrereqDeleteView.as_view(), name="prereq_delete"),
    url(r'^flaw/(?P<pk>[0-9]+)/', FlawUpdateView.as_view(), name="flaw_detail"),
    url(r'^flaw/new/', FlawCreateView.as_view(), name="flaw_create"),
    url(r'^flaw/', FlawListView.as_view(), name="flaws"),

    url(r'^prereq/delete/(?P<pk>[0-9]+)/', PrereqDeleteView.as_view(), name="prereq_delete"),
    url(r'^prereq/(?P<pk>[0-9]+)/', PrereqUpdateView.as_view(), name="prereq_detail"),
    url(r'^prereq/new/', PrereqCreateView.as_view(), name="prereq_create"),
    url(r'^prereq/', PrereqListView.as_view(), name="prereqs"),

    url('', ActionView.as_view(), name="home"),

]