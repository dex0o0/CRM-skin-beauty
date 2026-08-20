from django.shortcuts import render
from django.http import HttpResponse

def admin_custom(request):
    return render(request, 'admin_custom.html')
