from django.views.generic import View
from django.http import JsonResponse
from django import forms
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.forms.models import model_to_dict
from .models import Result

class  ResultForm(forms.ModelForm):
    class  Meta:
        model = Result
        fields =  '__all__'

class  ResultList(View):
    def  get(self, request):
        results =  list(Result.objects.all().values())
        data =  dict()
        data['results'] = results
        print(data)
        return JsonResponse(data)

