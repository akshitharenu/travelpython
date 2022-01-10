#from django.http import HttpResponse
from django.shortcuts import render
from . models import Person


# Create your views here.
def demo(request):
    obj=Person.objects.all()

    return render(request,"index.html",{'result':obj})
#def sum(request):
   # x=int(request.GET['num1'])
    #y=int(request.GET['num2'])
    #res=x+y
    #res1=x-y
    #res2=x*y
    #res3=x/y
    #return render(request,"result.html",{'result':[res,res1,res2,res3]})



