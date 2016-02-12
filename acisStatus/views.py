from django.shortcuts import render

def beamline_status(request):
	return render(request, 'acisStatus/status.html', {})
