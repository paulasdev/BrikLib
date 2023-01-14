from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Set
from .forms import SetForm


class SetListView(generic.ListView):
    model = Set
    template_name = 'index.html'
    paginate_by = 4


def search(request):
    """ search function  """
    if request.method == "POST":
        searched = request.POST['searched']
        sets = Set.objects.filter(theme__contains=searched)

        return render(request, 'search.html', {'searched': searched, 
                      'sets': sets})
    else: 
        return render(request, 'search.html', {})


def add_set(request):
    submitted = False
    if request.method == "POST":
        form = SetForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/add_set?submitted=True')
    else:
        form = SetForm
        if 'submitted' in request.GET:
            submitted = True
            
    return render(request, 'add_set.html', {'form': form, 
                'submitted': submitted})