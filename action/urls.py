from character.views import *
from action.views import *

"""action URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^characters/', CharacterListView.as_view(), name="characters"),
    url(r'^characters/<int:pk>/', CharacterDetailView.as_view(), name="character_detail"),
    url(r'^schticks/', SchtickListView.as_view(), name="schticks"),
    url(r'^schticks/<int:pk>/', SchtickDetailView.as_view(), name="schtick_detail"),
]
