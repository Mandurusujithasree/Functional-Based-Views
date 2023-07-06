from django.contrib import admin
from django.urls import path
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('passengers/',views.Passenger_list),
    path('passengers/<int:pk>/',views.Passenger_details),
]
