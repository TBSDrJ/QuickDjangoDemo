from django.urls import path
from .views import IndexView, DudeView

urlpatterns = [
    path('', IndexView.as_view(), name = 'index'),
    path('<dude>', DudeView.as_view(), name='dude'),
]
