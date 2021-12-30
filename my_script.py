from b_ball.models import Player

def delete_players():
        all =Player.objects.all()
        all.delete()


delete_players()