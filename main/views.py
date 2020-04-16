from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import List
from django.contrib import messages
from .forms import List_Forms

def index(request):
    if request.method == 'POST':
        form = List_Forms(request.POST or None)
        form.save()
        all_items = List.objects.all
        messages.success(request, 'Item has been added successfully.')
        return render(request, 'index.html', {'all_items': all_items})
    else:
        all_items = List.objects.all
        return render(request, 'index.html', {'all_items': all_items})

def delete(request, list_id):
    item = List.objects.get(pk = list_id)
    item.delete()
    messages.success(request, 'Item has been successfully deleted.')
    return redirect('index')

def cross_off(request, list_id):
    item = List.objects.get(pk = list_id)
    item.completed = True
    item.save()
    return redirect('index')

def uncross(request, list_id):
    item = List.objects.get(pk = list_id)
    item.completed = False
    item.save()
    return redirect('index')