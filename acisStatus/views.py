from django.shortcuts import render
from django.utils import timezone
from .models import Beamline


def beamline_status(request):
	beamlines = Beamline.objects.order_by('name')
	return render(request, 'acisStatus/status.html', 
		{'beamlines': beamlines})
