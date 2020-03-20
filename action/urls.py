from character.views import *
from action.views import SchtickListView, SchtickUpdateView, SchtickCreateView
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'characters/', CharacterListView.as_view(), name="characters"),
    path('characters/<int:pk>/attribute/', CharacterAttributeView.as_view(), name="character_attribute"),
    path('characters/<int:pk>/flaw/', CharacterFlawView.as_view(), name="character_flaw"),
    path('characters/<int:pk>/schtick/', CharacterSchtickView.as_view(), name="character_schtick"),
    path('characters/<int:pk>/skill/', CharacterSkillView.as_view(), name="character_skill"),
    path('characters/<int:pk>/', CharacterUpdateView.as_view(), name="character_detail"),

    path(r'schticks/', SchtickListView.as_view(), name="schticks"),
    path(r'schticks/new/', SchtickCreateView.as_view(), name="schtick_create"),
    path(r'schticks/<int:pk>/', SchtickUpdateView.as_view(), name="schtick_detail"),
]
