# import os
# from twilio.rest import Client
# from django.shortcuts import render
# from django.http import HttpResponseRedirect
# from .forms import TextAllPlayers
# from b_ball.models import Player_full_text_list


# def unlock2(request):
#     submitted = False
    
#     if request.method == "POST" and "all_players_list":
#         form = TextAllPlayers(request.POST)
#         if form.is_valid():
#             sms_to_full_list(form)
            
#             return HttpResponseRedirect('/')
#     else:
#         form = TextAllPlayers
#         if 'submitted' in request.GET:
#             submitted = True
    
#     return render(request, 'unlock.html', {'form': form, 'submitted': submitted})


# def sms_to_full_list():
#     message_to_send2 = form.cleaned_data['message']
#     account_sid = os.environ['TWILIO_ACCOUNT_SID']
#     auth_token = os.environ['TWILIO_AUTH_TOKEN']
#     client = Client(account_sid, auth_token)
#     all_players_cells_dict = Player_full_text_list.objects.values('player_name_full_text','player_cell_full_text')
#     all_players_list = []

#     for ele in all_players_cells_dict:
#         for key, value in ele.items():
#             v = value
#             all_players_list.append(v)

#     apl = {all_players_list[i]: all_players_list[i + 1] for i in range(0, len(all_players_list), 2)}
#     apl_value = list(apl.values())
#     all_players = apl_value
#     for p in all_players:
#         send_cell = p

#         message = client.messages \
#                         .create(
#                              body= message_to_send2,
#                              from_='+16467989631',
#                              to= '+1'+ send_cell,
#                     )
    
#         print(message.sid)