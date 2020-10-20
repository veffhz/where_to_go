from django.urls import path

from places.views import MainView, PlaceDetailView

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('place/<int:place_id>', PlaceDetailView.as_view(), name='place-detail'),
]
