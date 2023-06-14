from django.urls import path
from .views import *

urlpatterns = [
    path('', TicketAPIView.as_view()),
    path('region/', RegionAPIView.as_view()),
    path('city/', CityAPIView.as_view()),
    path('department/', DepartmentAPIView.as_view()),
    path('area/', AreaAPIView.as_view()),
]