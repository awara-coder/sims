from django.shortcuts import render
# Create your views here.


def index(request):
	if request.user.is_authenticated and request.user.is_activated == True:
		return render(request, 'index.html', {'is_activated' : True})
	elif request.user.is_authenticated and request.user.is_activated == False:
		return render(request, 'index.html', {'is_activated' : False})
	else:
		return render(request, 'index.html')