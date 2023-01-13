from django.shortcuts import render,redirect
from b_ball.sms_updates import sms_to_regist, sms_to_full_list
from .forms import PlayerForm, TextRegisteredPlayers, TextAllPlayers, TurnOff, EditPlayerForm, AllPlayersForm
from django.http import HttpResponseRedirect
from .models import Player, Player_full_text_list
from django.contrib.auth.decorators import login_required

def base(request):
    return render(request, 'base.html',{})

@login_required
def crud_base(request):
    players = Player.objects.all()
    all_players = Player_full_text_list.objects.all()
    count = len(players)
    count_all = len(all_players)
    return render (request, 'crud_base.html',{'players': players, 'all_players': all_players, 'count': count, 'count_all': count_all,})

def home(request):
    players = Player.objects.all()
    count = len(players)
    return render (request,'home.html',{'players': players, 'count': count,})

@login_required
def edit_roster(request,id):
    player = Player.objects.get(pk=id)
    form= EditPlayerForm(request.POST or None, instance = player)
    submitted= False
    if form.is_valid():
        form.save()
        return redirect('/crud_base')
    else:
        person = Player.objects.get(pk=id)
        form = EditPlayerForm(instance=person)
        return render(request,'edit_roster.html',{'form': form,})

@login_required
def edit_full_roster(request,id):
    player = Player_full_text_list.objects.get(pk=id)
    form= AllPlayersForm(request.POST or None, instance = player)
    submitted= False
    if form.is_valid():
        form.save()
        return redirect('/crud_base')
    else:
        person = Player_full_text_list.objects.get(pk=id)
        form = AllPlayersForm(instance=person)
        return render(request,'edit_full_roster.html',{'form': form,})

@login_required
def delete(request,id):   
    player = Player.objects.get(pk=id)
    player.delete()
    return redirect('/crud_base')

@login_required
def delete_full_list(request,id):
    player = Player_full_text_list.objects.get(pk=id)
    player.delete()
    return redirect('/crud_base')

# def update(request, id):
#     player = Player.objects.get(pk=id)
#     form= EditPlayerForm(request.POST)
#     if form.is_valid():
#         form.save()
#     return redirect('/edit_roster')

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

@login_required
def register_full_list(request):
    submitted = False
    if request.method == "POST":
        form = AllPlayersForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/crud_base')
    else:
        form = AllPlayersForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'register_full_list.html', {'form': form, 'submitted': submitted})

# def home(request):
#     players = Player.objects.all()
#     number_of_players = Player.objects.all()
#     count = len(number_of_players)
#     return render(request, 'home.html', {'players': players,'count':count,})

def too_many(request):
    return render(request, 'too_many.html', {})

@login_required
def sms_to_all(request):
    submitted = False
    if request.method == "POST":
        form = TextAllPlayers(request.POST)
        if form.is_valid():
            form = form.cleaned_data['message']
            sms_to_full_list(form)
                
            return HttpResponseRedirect('/crud_base')
    else:
        form = TextRegisteredPlayers
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'sms_to_all.html', {'form': form, 'submitted': submitted})

@login_required
def sms_to_registered(request):
    submitted = False        
    if request.method == "POST":
        form = TextRegisteredPlayers(request.POST)
        if form.is_valid():
            form = form.cleaned_data['message']
            sms_to_regist(form)
                    
            return HttpResponseRedirect('/crud_base')
    else:
        form = TextRegisteredPlayers
        if 'submitted' in request.GET:
            submitted = True
    
    return render(request, 'sms_to_registered.html', {'form': form, 'submitted': submitted})

@login_required
def send_texts(request):
    return render(request, 'send_texts.html', {})

@login_required
def on_off(request):
    toggle = TurnOff.objects.all()
    
    return render(request, 'on_off.html', {'toggle': toggle})

@login_required
def change_status(request,id):   
    flag = TurnOff.objects.get(pk=id)
    flag.on_off = 'True'
    flag.save()        
            
    return redirect('/crud_base')

@login_required
def turn_status_off(request, id):
    flag = TurnOff.objects.get(pk=id)
    flag.on_off = 'False'
    flag.save()        
            
    return redirect('/crud_base')
