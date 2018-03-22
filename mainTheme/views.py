from django.shortcuts import render

# Create your views here.

def index(request):
   return render(request, 'mainTheme/index.html', {} )

def service(request):
   return render(request, 'mainTheme/service.html', {} )

def contact(request):
   return render(request, 'mainTheme/contact.html', {} )
