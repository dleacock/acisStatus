from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.beamline_status, name='beamline_status'),
]