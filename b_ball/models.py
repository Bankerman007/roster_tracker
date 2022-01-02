from django.db import models

# Create your models here.
class Player(models.Model):
    player_name = models.CharField(max_length=30)
    player_email = models.CharField(max_length=30, default=123)
    player_cell = models.CharField(max_length=30, default=123)
    
    def __str__(self):
        return self.player_name