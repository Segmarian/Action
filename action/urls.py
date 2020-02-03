from character.views import CharacterListView, CharacterUpdateView
from action.views import SchtickListView, SchtickUpdateView
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'characters/', CharacterListView.as_view(), name="characters"),
    path('characters/<int:pk>/', CharacterUpdateView.as_view(), name="character_detail"),
    path(r'schticks/', SchtickListView.as_view(), name="schticks"),
    path(r'schticks/<int:pk>/', SchtickUpdateView.as_view(), name="schtick_detail"),
]
