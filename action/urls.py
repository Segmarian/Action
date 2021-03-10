from django.contrib import admin
from django.conf.urls import url
from action.views import *
from character.views import *

urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'^characters/(?P<pk>[0-9]+)/attribute/', CharacterAttributeView.as_view(),
         name="characterattribute"),
    url(r'^characters/(?P<pk>[0-9]+)/flaw/', CharacterFlawView.as_view(), name="characterflaw"),
    url(r'^characters/(?P<pk>[0-9]+)/schtick/', CharacterSchtickView.as_view(), name="characterschtick"),
    url(r'^characters/(?P<pk>[0-9]+)/basic/', CharacterBasicView.as_view(), name="characterbasic"),

    url(r'^characters/(?P<pk>[0-9]+)/', CharacterDetailView.as_view(), name="characterdetail"),
    url(r'^characters/new/', CharacterCreateView.as_view(), name="charactercreate"),
    url(r'^characters/', CharacterListView.as_view(), name="characters"),
    url('', CharacterListView.as_view(), name="home"),

    url(r'^class/', CharacterClassListView.as_view(), name='characterclasslist'),
    url(r'^class/(?P<pk>[0-9]+)/', CharacterClassUpdateView.as_view(), name='characterclassupdate'),
    url(r'^class/new/', CharacterClassCreateView.as_view(), name='characterclassupdate'),
    url(r'^class/entry/', ClassEntryListView.as_view(), name='classentrylist'),
    url(r'^class/entry/(?P<pk>[0-9]+)/', ClassEntryUpdateView.as_view(), name='classentryupdate'),
    url(r'^class/entry/new/', ClassEntryCreateView.as_view(), name='classentrycreate'),
    url(r'^schtick/', SchtickListView.as_view(), name="schticks"),
    url(r'^schtick/new/', SchtickCreateView.as_view(), name="schtick_create"),
    url(r'^schtick/(?P<pk>[0-9]+)/', SchtickUpdateView.as_view(), name="schtick_detail"),
]
