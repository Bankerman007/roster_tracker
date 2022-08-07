from django.shortcuts import render,redirect
from b_ball.sms_updates import sms_to_regist, sms_to_full_list
from .forms import PlayerForm, TextRegisteredPlayers, TextAllPlayers, TurnOff
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

def sms_to_all(request):
    submitted = False
    if request.method == "POST":
        form = TextAllPlayers(request.POST)
        if form.is_valid():
            form = form.cleaned_data['message']
            sms_to_full_list(form)
                
            return HttpResponseRedirect('/')
    else:
        form = TextRegisteredPlayers
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'sms_to_all.html', {'form': form, 'submitted': submitted})

def sms_to_registered(request):
    submitted = False        
    if request.method == "POST":
        form = TextRegisteredPlayers(request.POST)
        if form.is_valid():
            form = form.cleaned_data['message']
            sms_to_regist(form)
                    
            return HttpResponseRedirect('/')
    else:
        form = TextRegisteredPlayers
        if 'submitted' in request.GET:
            submitted = True
    
    return render(request, 'sms_to_registered.html', {'form': form, 'submitted': submitted})

def send_texts(request):
    return render(request, 'send_texts.html', {})

def on_off(request):
           
    toggle = TurnOff.objects.all()
    
    return render(request, 'on_off.html', {'toggle': toggle})

def change_status(request,id):   
    flag = TurnOff.objects.get(pk=id)
    flag.on_off = 'True'
    flag.save()        
            
    return redirect('/on_off')

def turn_status_off(request, id):
    flag = TurnOff.objects.get(pk=id)
    flag.on_off = 'False'
    flag.save()        
            
    return redirect('/on_off')
