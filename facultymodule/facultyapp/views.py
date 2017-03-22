from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ViewForm


def email(request):
    if request.method == 'GET':
        form = ViewForm()
    else:
        form = ViewForm(request.POST)
        if form.is_valid():
            Student_ID = form.cleaned_data['Student_ID']
            Notifications = form.cleaned_data['Notifications']
           
            return redirect('success')
    return render(request, "next.html", {'form': form})


def success(request):
    return HttpResponse('Success! Notifications Updated.')
