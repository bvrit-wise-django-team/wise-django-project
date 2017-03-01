from django.shortcuts import render
from django.template.response import TemplateResponse
from polls.models import Person
from forms import *
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.
def name(request):
        return render(request, 'name.html')

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PersonForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            first_name = request.POST.get('first_name', '')
            last_name = request.POST.get('last_name', '')
            person_obj = Person(first_name = first_name, last_name = last_name)
            person_obj.save()

            return HttpResponseRedirect('/polls/viewNames/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PersonForm()

    return render(request, 'name.html', {'form': form})

'''
def get_name(request):
	data = Person.objects.all()
	print(data)
	return TemplateResponse(request, "name.html", {"data": data})
'''

def viewNames(request):
        return render(request, 'viewNames.html')


