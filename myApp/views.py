from django.shortcuts import render
from django.urls.converters import StringConverter

# Create your views here.
def helloworldview(request):
    string = "everyone"
    context = {'string' : string}
    return render(request, 'helloworld.html', context)