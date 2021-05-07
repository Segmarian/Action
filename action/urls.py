from django.contrib import admin
from django.conf.urls import url
from action.views import *
from character.views import *

urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'^character/(?P<pk>[0-9]+)/attribute/', CharacterAttributeView.as_view(),
         name="characterattribute"),
    url(r'^character/(?P<pk>[0-9]+)/flaw/', CharacterFlawView.as_view(), name="characterflaw"),
    url(r'^character/(?P<pk>[0-9]+)/schtick/', CharacterSchtickView.as_view(), name="characterschtick"),
    url(r'^character/(?P<pk>[0-9]+)/basic/', CharacterBasicView.as_view(), name="characterbasic"),

    url(r'^character/(?P<pk>[0-9]+)/', CharacterDetailView.as_view(), name="characterdetail"),
    url(r'^character/new/', CharacterCreateView.as_view(), name="charactercreate"),
    url(r'^character/', CharacterListView.as_view(), name="characters"),

    url(r'^charclass/(?P<pk>[0-9]+)/', CharacterClassUpdateView.as_view(), name='characterclassupdate'),
    url(r'^charclass/new/', CharacterClassCreateView.as_view(), name='characterclassupdate'),
    url(r'^charclass/entry/(?P<pk>[0-9]+)/', ClassEntryUpdateView.as_view(), name='classentryupdate'),
    url(r'^charclass/entry/new/', ClassEntryCreateView.as_view(), name='classentrycreate'),
    url(r'^charclass/entry/', ClassEntryListView.as_view(), name='classentrylist'),
    url(r'^charclass/', CharacterClassListView.as_view(), name='characterclasslist'),
    url(r'^schtick/(?P<pk>[0-9]+)/', SchtickUpdateView.as_view(), name="schtick_detail"),
    url(r'^schtick/new/', SchtickCreateView.as_view(), name="schtick_create"),
    url(r'^schticktype/(?P<pk>[0-9]+)/', SchtickTypeUpdateView.as_view(), name="schtick_type_detail"),
    url(r'^schticktype/new/', SchtickTypeCreateView.as_view(), name="schtick_type_create"),
    url(r'^schtick/', SchtickListView.as_view(), name="schticks"),
    url('', CharacterListView.as_view(), name="home"),
    '''url(r'^schtick/type/', SchtickTypeListView.as_view(), name="schtick_type"),'''
]
