from django.contrib import admin
from django.urls import path

from fire.views import HomePageView, ChartView, PieCountbySeverity, LineCountbyMonth, MultilineIncidentTop3Country, multipleBarbySeverity, fire_incidents_map, delete_location, IncidentList, IncidentCreateView, IncidentUpdateView, IncidentDeleteView, LocationsList, LocationsCreateView, LocationsUpdateView, LocationsDeleteView, FireStationList, FireStationCreateView, FireStationUpdateView, FireStationDeleteView, FireFightersList, FireFightersCreateView, FireFightersUpdateView, FireFightersDeleteView, FireTruckList, FireTruckCreateView, FireTruckUpdateView, FireTruckDeleteView, WeatherConditionsList, WeatherConditionsCreateView, WeatherConditionsUpdateView, WeatherConditionsDeleteView
from fire import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('dashboard_chart', ChartView.as_view(), name='dashboard-chart'),
    path('PieChart/', PieCountbySeverity, name='chart'),
    path('lineChart/', LineCountbyMonth, name='chart'),
    path('multilineChart/', MultilineIncidentTop3Country, name='chart'),
    path('multiBarChart/', multipleBarbySeverity, name='chart'),
    path('stations', views.map_station, name='map-station'),
    path('fire_incidents_map/', views.fire_incidents_map, name='fire_incidents_map'),
    path('database/', views.database_view, name='database'),
    path('delete/<int:location_id>/', delete_location, name='delete_location'),

    path('firestation_list', FireStationList.as_view(), name='firestation-list'),
    path('firestation_list/add', FireStationCreateView.as_view(), name='firestation-add'),
    path('firestation_list/<pk>', FireStationUpdateView.as_view(), name='firestation-update'),
    path('firestation_list/<pk>/delete', FireStationDeleteView.as_view(), name='firestation-delete'),

    path('incidents/', IncidentList.as_view(), name='incident-list'),
    path('incidents/add/', IncidentCreateView.as_view(), name='incident-add'),
    path('incidents/<pk>/', IncidentUpdateView.as_view(), name='incident-update'),
    path('incidents/<pk>/delete/', IncidentDeleteView.as_view(), name='incident-delete'),

    path('locations/', LocationsList.as_view(), name='locations-list'),
    path('locations/add/', LocationsCreateView.as_view(), name='locations-add'),
    path('locations/<pk>/', LocationsUpdateView.as_view(), name='locations-update'),
    path('locations/<pk>/delete/', LocationsDeleteView.as_view(), name='locations-delete'),

    path('firefighters/', FireFightersList.as_view(), name='firefighters-list'),
    path('firefighters/add/', FireFightersCreateView.as_view(), name='firefighters-add'),
    path('firefighters/<pk>/', FireFightersUpdateView.as_view(), name='firefighters-update'),
    path('firefighters/<pk>/delete/', FireFightersDeleteView.as_view(), name='firefighters-delete'),

    path('firetrucks/', FireTruckList.as_view(), name='firetruck-list'),
    path('firetrucks/add/', FireTruckCreateView.as_view(), name='firetruck-add'),
    path('firetrucks/<pk>/', FireTruckUpdateView.as_view(), name='firetruck-update'),
    path('firetrucks/<pk>/delete/', FireTruckDeleteView.as_view(), name='firetruck-delete'),

    path('weather/', WeatherConditionsList.as_view(), name='weather-list'),
    path('weather/add/', WeatherConditionsCreateView.as_view(), name='weather-add'),
    path('weather/<pk>/', WeatherConditionsUpdateView.as_view(), name='weather-update'),
    path('weather/<pk>/delete/', WeatherConditionsDeleteView.as_view(), name='weather-delete'),

]