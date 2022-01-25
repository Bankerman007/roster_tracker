from django.db import models

# Create your models here.
class Player(models.Model):
    player_name = models.CharField(max_length=30)
    player_email = models.CharField(max_length=30)
    player_cell = models.CharField(max_length=10)
    
    def __str__(self):
        return self.player_name

class Player_full_text_list(models.Model):
    player_name_full_text = models.CharField(max_length=30)
    player_cell_full_text = models.CharField(max_length=30)

    def __str__(self):
        return self.player_name_full_text