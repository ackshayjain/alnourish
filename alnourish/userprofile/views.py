from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
# import requests

# Create your views here
from .models import Culture
from .forms import AddForm
from django.shortcuts import render,redirect

# Create your views here.


@login_required(login_url='/account/login/')
def index(request):
    return render(request, 'userprofile/track.html')


def new_culture(request):
    if request.method == 'POST':
        # create a form instance and popuslate it with data from the request:
        form = AddForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            username = request.user.username
            name = request.POST.get('name', '')
            volume = request.POST.get('volume', '')
            culture_obj = Culture(username=username,name=name,volume=volume)
            culture_obj.save()
            return redirect('profile:index')
            # return render(request, 'ES/index2.html', context)

        # if a GET (or any other method) we'll create a blank form
    else:
        form = AddForm()

    context = {'form': form}

    return render(request, 'userprofile/new.html', context)