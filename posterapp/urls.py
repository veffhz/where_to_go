from django.urls import path

from posterapp.views import MainView

urlpatterns = [
    path('', MainView.as_view(), name='main'),
]
