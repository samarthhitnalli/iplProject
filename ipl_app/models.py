from django.db import models
# ipl_app/models.py

class Admin(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.username

class CricketBoard(models.Model):
    board_name = models.CharField(max_length=200)
    team = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='teams/',)  # Add logo field

    def __str__(self):
        return self.team

class Player(models.Model):
    name = models.CharField(max_length=100)
    team = models.ForeignKey(CricketBoard, on_delete=models.CASCADE)
    role = models.CharField(max_length=50)
    matches_played = models.IntegerField()
    runs_scored = models.IntegerField()
    wickets_taken = models.IntegerField()
    image = models.ImageField(upload_to='players/')

    def __str__(self):
        return self.name

class Stadium(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    capacity = models.IntegerField()
    image = models.ImageField(upload_to='stadiums/')

    def __str__(self):
        return self.name

class Schedule(models.Model):
    match_date = models.DateField()
    team1 = models.ForeignKey(CricketBoard, related_name='team1', on_delete=models.CASCADE)
    team2 = models.ForeignKey(CricketBoard, related_name='team2', on_delete=models.CASCADE)
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.team1} vs {self.team2} on {self.match_date}"
