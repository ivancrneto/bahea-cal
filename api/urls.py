from django.urls import path
from api import views, view_cors

urlpatterns = [
    path('v1/calendar/init/', views.calendar_init_view, name='calendar_init'),
    # path('v1/calendar/flow/', views.calendar_flow_view, name='calendar_flow'),
    path('v1/calendar/token/', views.calendar_token, name='calendar_token'),
    path('v1/cors/test', view_cors.cors_test, name='cors_test'),
]

