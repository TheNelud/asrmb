from django.shortcuts import render

# Create your views here.
def mar(request):
   
    return render(request, 'mar.html')


def mag(request):
       
    return render(request, 'mag.html')

def sar(request):
       
    return render(request, 'sar.html')