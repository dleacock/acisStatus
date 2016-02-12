from django.shortcuts import render
from django.shortcuts import render_to_response
from .models import Beamline


def beamline_status(request):
	beamline_list = Beamline.objects.order_by('name')
	context_dict = {'beamlines:' beamline_list}
	return render(request, 'acisStatus/status.html', context_dict)
