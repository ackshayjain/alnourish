from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
# import requests
from django import forms
# Create your views here
from .models import Culture
from .forms import AddForm
from django.shortcuts import render,redirect

# Create your views here.


@login_required(login_url='/account/login/')
def index(request):
    username = request.user.username
    cultures_qs = Culture.objects.filter(username=username)
    context = {'cultures':cultures_qs}
    return render(request, 'userprofile/track.html',context)

@login_required(login_url='/account/login/')
def new_culture(request):
    if request.method == 'POST':

        form = AddForm(request.POST)

        if form.is_valid():
            username = request.user.username
            name = request.POST.get('name', '')
            volume = request.POST.get('volume', '')
            culture_qs = Culture.objects.filter(username=username, name=name)
            if culture_qs.exists():
                errors = "This culture already exists"
                form=AddForm()
                context = {'form': form, 'errors': errors}
                return render(request, 'userprofile/new.html', context)
            else:
                culture_obj = Culture(username=username, name=name, volume=volume)

                culture_obj.save()
                return redirect('profile:index')




    else:
        form = AddForm()

    context = {'form': form}

    return render(request, 'userprofile/new.html', context)