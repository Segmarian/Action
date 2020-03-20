from character.views import *
from action.views import SchtickListView, SchtickUpdateView, SchtickCreateView
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'characters/', CharacterListView.as_view(), name="characters"),
    url('characters/<int:pk>/attribute/', CharacterAttributeView.as_view(), name="character_attribute"),
    url('characters/<int:pk>/flaw/', CharacterFlawView.as_view(), name="character_flaw"),
    url('characters/<int:pk>/schtick/', CharacterSchtickView.as_view(), name="character_schtick"),
    url('characters/<int:pk>/skill/', CharacterSkillView.as_view(), name="character_skill"),
    url('characters/<int:pk>/', CharacterUpdateView.as_view(), name="character_detail"),

    url(r'schticks/', SchtickListView.as_view(), name="schticks"),
    url(r'schticks/new/', SchtickCreateView.as_view(), name="schtick_create"),
    url(r'schticks/<int:pk>/', SchtickUpdateView.as_view(), name="schtick_detail"),
]
