from django.urls import path

from weather_template_app import views

urlpatterns = [path("", views.WeatherInfoView.as_view(), name="home")]
