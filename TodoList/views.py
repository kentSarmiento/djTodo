from django.shortcuts import render
from .models import List
from .forms import ListForm

# Create your views here.
def home(request):
    context={}

    if request.method == 'POST':
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = List.objects.all
            context={'all_items': all_items}

        return render(request, 'home.html', context)

    else:
        all_items = List.objects.all
        context={'all_items': all_items}
        return render(request, 'home.html', context)