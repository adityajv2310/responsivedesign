from django.shortcuts import render

# Create your views here.

def productsresposive(request):
    context = {}
    return render(request,'responsivewebsite/productsresponsive.html',context)