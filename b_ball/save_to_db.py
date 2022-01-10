from b_ball.models import Player
from b_ball.models import Player_full_text_list



def start_db_save():
    this_weeks_players_dict = Player.objects.values('player_name', 'player_cell')
    this_weeks_list = []

    for ele in this_weeks_players_dict:
        for key, value in ele.items():
            v = value
            this_weeks_list.append(v)

    twl = {this_weeks_list[i]: this_weeks_list[i + 1] for i in range(0, len(this_weeks_list), 2)}
    twl_value = list(twl.values())
        

    all_players_cells_dict = Player_full_text_list.objects.values('player_name_full_text','player_cell_full_text')
    all_players_list = []

    for ele in all_players_cells_dict:
        for key, value in ele.items():
            v = value
            all_players_list.append(v)

    apl = {all_players_list[i]: all_players_list[i + 1] for i in range(0, len(all_players_list), 2)}
    apl_value = list(apl.values())
        

    missing = set(twl_value).difference(apl_value)
    for m in missing:
        add_player = Player.objects.get(player_cell = m)    
        add = Player_full_text_list(player_name_full_text= add_player, player_cell_full_text = m)
        add.save()
      
    return [twl_value,apl_value]
    




        
       
    
  
   

    
    


    