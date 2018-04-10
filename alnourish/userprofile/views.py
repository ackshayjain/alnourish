from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
# import requests

# Create your views here
# from .models import Test
# from .forms import AddForm
from django.shortcuts import render

# Create your views here.


@login_required(login_url='/account/login/')
def index(request):
    return render(request, 'userprofile/track.html')