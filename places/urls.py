from django.urls import path

from places.views import MainView

urlpatterns = [
    path('', MainView.as_view(), name='main'),
]
