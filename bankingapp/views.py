from django.shortcuts import render

# Create your views here.
def slip(request):
    return render(request,'deposited_slip.html',{})