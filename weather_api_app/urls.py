from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from weather_api_app import views

urlpatterns = [
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="docs",
    ),
    path("weather/", views.WeatherInfoAPIView.as_view(), name="weather_api"),
]
