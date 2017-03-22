from django.http import HttpResponse

def index(request):
    return HttpResponse("MoviesAPP::Hello world!")
# Create your views here.
