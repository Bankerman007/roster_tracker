from django.shortcuts import render

# Create your views here.
# from django.shortcuts import redirect, render
# from v_ball.teams_total_points import total_point_calc
# from v_ball.prep_players import prep_players
# from .forms import PlayerForm
# from django.http import HttpResponseRedirect
# from .models import Player
# from v_ball.make_teams import main


def base(request):
    return render(request, 'base.html',{})


# def delete_players(request):
#         players = Player.objects.all()
#         return render(request,'delete_players.html',{'players':players})

# def register(request):
#     submitted = False
#     if request.method == "POST":
#         form = PlayerForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/success')
#     else:
#         form = PlayerForm
#         if 'submitted' in request.GET:
#             submitted = True
#     return render(request, 'register.html', {'form': form, 'submitted': submitted})

# def home(request):
#     [red_team_points, blue_team_points, black_team_points, green_team_points, brown_team_points] = total_point_calc()
#     players1 = Player.objects.all().filter(team = 1)
#     players2 = Player.objects.all().filter(team = 2)
#     players3 = Player.objects.all().filter(team = 3)
#     players4 = Player.objects.all().filter(team = 4)
#     players5 = Player.objects.all().filter(team = 5)
#     points_red = red_team_points
#     points_blue = blue_team_points
#     points_black = black_team_points
#     points_green = green_team_points
#     points_brown = brown_team_points