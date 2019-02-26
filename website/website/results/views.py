from django.views.generic import View
from django.http import JsonResponse
from django import forms
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.forms.models import model_to_dict
from .models import *

class  ResultForm(forms.ModelForm):
    class  Meta:
        model = Result
        fields =  '__all__'

class  ResultList(View):
    def  get(self, request):
        #results = Result.objects.raw('SELECT results_result.id, value, games.name AS game_name, auth_user.username AS user_name FROM results_result LEFT JOIN games ON games.id = results_result.idGame LEFT JOIN auth_user ON auth_user.id = results_result.idUser')
        results = Result.objects.select_related('game', 'user')

        value_list = list()
        for row in results:
        	row_dict = dict()
        	row_dict['value'] = row.value
        	row_dict['game_name'] = row.game.name
        	row_dict['user_name'] = row.user.username
        	value_list.append(row_dict)
        data = dict()
        data['results'] = value_list
        # {'results': [{'id': 1, 'value': 10, 'idGame': 1, 'idUser': 1, 'date': datetime.datetime(2019, 2, 21, 22, 10, 3, tzinfo=<UTC>)}, 
        # {'id': 2, 'value': 39, 'idGame': 2, 'idUser': 2, 'date': datetime.datetime(2019, 2, 23, 23, 6, 27, tzinfo=<UTC>)}]}
        #{'results': [{'value': 10, 'game_name': 'game1', 'user_name': 'admin'}, {'value': 39, 'game_name': 'game2', 'user_name': 'inka'}]}
        return JsonResponse(data)

