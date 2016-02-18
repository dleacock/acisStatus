from django.shortcuts import render
from django.utils import timezone
from .models import Beamline


def beamline_status(request):
	beamlines = Beamline.objects.order_by('storage_ring_order')
	return render(request, 'acisStatus/status.html', 
		{'beamlines': beamlines})
