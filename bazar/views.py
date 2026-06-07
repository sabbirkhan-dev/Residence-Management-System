from django.shortcuts import render

# Create your views here.

def bazar_list(request):
    return render(request, 'bazar/list.html')