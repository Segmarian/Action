from character.views import *
from django.urls import path
from action.views import SchtickListView, SchtickUpdateView, SchtickCreateView, CharacterClassUpdateView, \
    CharacterClassCreateView, ClassEntryListView, ClassEntryUpdateView, ClassEntryCreateView, CharacterClassListView
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('characters/<int:pk>/attribute/', CharacterAttributeView.as_view(), name="character_attribute"),
    path('characters/<int:pk>/flaw/', CharacterFlawView.as_view(), name="character_flaw"),
    path('characters/<int:pk>/schtick/', CharacterSchtickView.as_view(), name="character_schtick"),
    path('characters/<int:pk>/skill/', CharacterSkillView.as_view(), name="character_skill"),
    path('characters/<int:pk>/', CharacterUpdateView.as_view(), name="character_detail"),
    path('characters/', CharacterListView.as_view(), name="characters"),
    path('', CharacterListView.as_view(), name="home"),

    path(r'class/', CharacterClassListView.as_view(), name='characterclasslist'),
    path(r'class/<int:pk>/', CharacterClassUpdateView.as_view(), name='characterclassupdate'),
    path(r'class/new/>', CharacterClassCreateView.as_view(), name='characterclassupdate'),
    path(r'class/entry', ClassEntryListView.as_view(), name='classentrylist'),
    path(r'class/entry/<int:pk>', ClassEntryUpdateView.as_view(), name='classentryupdate'),
    path(r'class/entry/new', ClassEntryCreateView.as_view(), name='classentrycreate'),
    path(r'schtick/', SchtickListView.as_view(), name="schticks"),
    path(r'schtick/new/', SchtickCreateView.as_view(), name="schtick_create"),
    path(r'schtick/<int:pk>/', SchtickUpdateView.as_view(), name="schtick_detail"),
]
