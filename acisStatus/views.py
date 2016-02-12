from django.shortcuts import render
from django.utils import timezone
from .models import Beamline


def beamline_status(request):
	beamlines = Beamline.objects.filter(updated_date__lte=timezone.now()).order_by('updated_date')
	return render(request, 'acisStatus/status.html', 
		{'beamlines': beamlines})
