from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import Add_expense_form
from .models import Tracker_model
# Create your views here.
def Add_expense(request):
    form=Add_expense_form()
    if request.method=="POST":
        form=Add_expense_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/read/')
    return render(request,'add_expense.html',{'form':form})

def Read_expense(request):
    obj=Tracker_model.objects.all()
    return render(request,'read.html',{'obj':obj})