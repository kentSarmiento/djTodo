from django.shortcuts import render, redirect
from django.contrib import messages
from .models import List
from .forms import ListForm

# Create your views here.
def home(request):
    context={}

    if request.method == 'POST':
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, ('Task is successfully added!'))
            all_items = List.objects.filter(completed=False)
            context={'all_items': all_items}
        else:
            messages.warning(request, ('Task is NOT added!'))

        return render(request, 'home.html', context)

    else:
        all_items = List.objects.filter(completed=False)
        context={'all_items': all_items}
        return render(request, 'home.html', context)

def archive(request):
    all_items = List.objects.filter(completed=True)
    context={'all_items': all_items, 'archived': True}
    return render(request, 'home.html', context)

def done(request, id):
    item = List.objects.get(pk=id)
    item.completed = True
    item.save()
    return redirect('home')

def undone(request, id):
    item = List.objects.get(pk=id)
    item.completed = False
    item.save()
    return redirect('home')

def edit(request, id):
    context={}

    if request.method == 'POST':
        item = List.objects.get(pk=id)
        form = ListForm(request.POST or None, instance=item)

        if form.is_valid():
            form.save()
            messages.success(request, ('Task is successfully updated!'))
            all_items = List.objects.all
            context={'all_items': all_items}
        else:
            messages.warning(request, ('Task is NOT updated!'))

        return redirect('home')

    else:
        item = List.objects.get(pk=id)
        context = {'item': item}

        return render(request, 'edit.html', context)

def delete(request, id):
    item = List.objects.get(pk=id)
    item.delete()
    return redirect('home')
