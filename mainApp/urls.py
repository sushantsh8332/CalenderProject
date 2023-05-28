from django.urls import path
from . import views

urlpatterns = [
    path('init/', views.GoogleCalendarInitView, name='googleCalendarInit'),
    path('redirect/', views.GoogleCalendarRedirectView, name='googleCalendarRedirect')
]