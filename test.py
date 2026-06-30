import requests
BASE_URL = 'http://127.0.0.1:8000/' 
ENDPOINT = 'comapi'
res_ponse = requests.get(BASE_URL+ENDPOINT)
data_fetch = res_ponse.json()
print("Data fetch from Django Application")
print('-'*50)
print('book_name: ',data_fetch['book_name']) 
print('author_name: ',data_fetch['author_name'])
print('edition: ',data_fetch['edition'])