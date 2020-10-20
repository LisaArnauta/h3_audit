from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('my_audits', views.my_audits, name='my_audits'),
    path('registration', views.registration, name='registrations')
]