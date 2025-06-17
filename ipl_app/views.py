from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Player, Schedule, Stadium, CricketBoard
from .forms import PlayerForm, ScheduleForm, StadiumForm, CricketBoardForm

def home(request):
    return render(request, 'ipl_app/home.html')

def about(request):
    return render(request, 'ipl_app/about.html')

def add_player(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PlayerForm()
    return render(request, 'ipl_app/add_player.html', {'form': form})

def add_schedule(request):
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ScheduleForm()
    return render(request, 'ipl_app/add_schedule.html', {'form': form})

def add_stadium(request):
    if request.method == 'POST':
        form = StadiumForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StadiumForm()
    return render(request, 'ipl_app/add_stadium.html', {'form': form})

def add_team(request):
    if request.method == 'POST':
        form = CricketBoardForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CricketBoardForm()
    return render(request, 'ipl_app/add_team.html', {'form': form})

def list_players(request):
    players = Player.objects.all()
    return render(request, 'ipl_app/list_players.html', {'players': players})

def list_schedules(request):
    schedules = Schedule.objects.all()
    return render(request, 'ipl_app/list_schedules.html', {'schedules': schedules})

def list_stadiums(request):
    stadiums = Stadium.objects.all()
    return render(request, 'ipl_app/list_stadiums.html', {'stadiums': stadiums})


from django.shortcuts import render, redirect
from .forms import CricketBoardForm



def team_list(request):
    teams = CricketBoard.objects.all()
    return render(request, 'ipl_app/team_list.html', {'teams': teams})
