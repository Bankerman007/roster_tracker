from django.shortcuts import render,redirect

# Create your views here.
# from django.shortcuts import redirect, render
from .forms import PlayerForm
from django.http import HttpResponseRedirect
from .models import Player



def base(request):
    return render(request, 'base.html',{})


def edit_roster(request):
         players = Player.objects.all()
         return render(request,'edit_roster.html',{'players':players})

def delete(request,id):   
        player = Player.objects.get(pk=id)
        player.delete()
        return redirect('/')

def register_player(request):
    submitted = False
    players = Player.objects.all()
    count = len(players)
    if count == 15:
        return HttpResponseRedirect('/too_many')
    elif request.method == "POST":
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = PlayerForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'register_player.html', {'form': form, 'submitted': submitted})

def home(request):
    players = Player.objects.all()
    number_of_players = Player.objects.all()
    count = len(number_of_players)
    return render(request, 'home.html', {'players': players,'count':count,})

def too_many(request):
    return render(request, 'too_many.html', {})