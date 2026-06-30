from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def algobooks_view(request):
    algobooks_data={
        'book_name' : 'Grokking Algorithms',
        'author_name' : 'Aditya Y. Bhargava',  
        'edition' : 2,
    }
    algobooks_response = '<h2> book_name:{} <br> author_name:{} <br> edition:{} </h2>'.format(algobooks_data['book_name'], algobooks_data['author_name'], algobooks_data['edition'])
    return HttpResponse(algobooks_response)

import json
def algobooks_json_view(request):
    algobooks_data={
        'book_name' : 'Grokking Algorithms',
        'author_name' : 'Aditya Y. Bhargava',  
        'edition' : 2,
    }
    json_data = json.dumps(algobooks_data)
    return HttpResponse(json_data, content_type='application/json')

from django.http import JsonResponse
def algobooks_json_view2(request):
    algobooks_data={
        'book_name': 'Grokking Algorithms',
        'author_name' : 'Aditya Y. Bhargava',  
        'edition' : 2,
    }
    return JsonResponse(algobooks_data)

from django.views.generic import View
class Jsoncommunication(View):
    def get(self, request, *args, **kwargs):
        algobooks_data={
        'book_name': 'Grokking Algorithms',
        'author_name' : 'Aditya Y. Bhargava',  
        'edition' : 2,
        }
        return JsonResponse(algobooks_data)
