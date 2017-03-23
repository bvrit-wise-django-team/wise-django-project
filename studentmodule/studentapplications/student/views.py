from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ViewForm
from  student.models import StudentContactDetails


def index(request):
    if request.method == "POST":
        form = ViewForm(request.POST) 
        if form.is_valid():
		//get cleaned data
            StudentContactDetails = form.save(commit = False)
            StudentContactDetails.save()            
            return redirect('success')
        
    else:
        form = ViewForm()
    return render(request, "index.html", {'form': form})


def success(request):
    return HttpResponse('Success!Updated.')