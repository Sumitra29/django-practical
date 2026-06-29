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
