from b_ball.models import Player

def delete_players():
        players = Player.objects.all()
        players.delete()

delete_players()