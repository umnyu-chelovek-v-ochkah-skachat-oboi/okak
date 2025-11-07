from django.shortcuts import render
from django.http import HttpResponse
from .models import Table
from .forms import TableForm

def text(request):
    table=Table.objects.all()
    return render(request, "main/home.html", {'table':table})
def text2(request):
    if request.method=='POST':
        form=TableForm(request.POST)
        form.save()
    form = TableForm()
    context={'form':form}
    return render(request, "main/testo.html", context)