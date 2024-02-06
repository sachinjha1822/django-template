from django.shortcuts import render

# Create your views here.

def htmlform(request):
    return render(request,"app/forms.html")