from django.shortcuts import render

# Create your views here.


def index(request):
	return render(request,'index.html')

def about(request):
	return render(request,'AboutUs.html')

def contact(request):
	return render(request,'ContactUs.html')

def login(request):
	return render(request,'Login.html')
	
def register(request):
	return render(request,'Register.html')
	
	
	