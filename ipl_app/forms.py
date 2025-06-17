from django import forms
from .models import Player, Schedule, Stadium,CricketBoard

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['name', 'team', 'role', 'matches_played', 'runs_scored', 'wickets_taken','image']

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['match_date', 'team1', 'team2', 'stadium']
        widgets = {
            'match_date': forms.DateInput(attrs={'type': 'date'})}

class StadiumForm(forms.ModelForm):
    class Meta:
        model = Stadium
        fields = ['name', 'location', 'capacity','image']

class CricketBoardForm(forms.ModelForm):
    class Meta:
        model = CricketBoard
        fields = ['team', 'logo']