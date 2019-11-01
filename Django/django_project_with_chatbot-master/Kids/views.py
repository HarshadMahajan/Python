from django.shortcuts import render
from . models import ICC

def index(request):
    context = ICC.objects.all()
    context = {'stat_data':context}
    return render(request,'Kids/index.html',context)
# Create your views here.
