from django.contrib import admin
from django.urls import path

from action.views import *
from character.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('characters/<int:pk>/attribute/', CharacterAttributeView.as_view(),
         name="characterattribute"),
    path('characters/<int:pk>/flaw/', CharacterFlawView.as_view(), name="characterflaw"),
    path('characters/<int:pk>/schtick/', CharacterSchtickView.as_view(), name="characterschtick"),
    path('characters/<int:pk>/basic/', CharacterBasicView.as_view(), name="characterbasic"),
    path('characters/<int:pk>/', CharacterDetailView.as_view(), name="characterdetail"),
    path('characters/new/', CharacterCreateView.as_view(), name="charactercreate"),
    path('characters/', CharacterListView.as_view(), name="characters"),
    path('$', CharacterListView.as_view(), name="home"),

    path(r'class/$', CharacterClassListView.as_view(), name='characterclasslist'),
    path(r'class/<int:pk>/', CharacterClassUpdateView.as_view(), name='characterclassupdate'),
    path(r'class/new/$', CharacterClassCreateView.as_view(), name='characterclassupdate'),
    path(r'class/entry/$', ClassEntryListView.as_view(), name='classentrylist'),
    path(r'class/entry/<int:pk>/', ClassEntryUpdateView.as_view(), name='classentryupdate'),
    path(r'class/entry/new/', ClassEntryCreateView.as_view(), name='classentrycreate'),
    path(r'schtick/$', SchtickListView.as_view(), name="schticks"),
    path(r'schtick/new/$', SchtickCreateView.as_view(), name="schtick_create"),
    path(r'schtick/<int:pk>/', SchtickUpdateView.as_view(), name="schtick_detail"),
]
