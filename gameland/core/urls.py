from unicodedata import name
from django.urls import path
from .views import home, select_char



urlpatterns = [
    path('', home, name="home"),
    path('characters/', select_char, name='character_select'),
]
