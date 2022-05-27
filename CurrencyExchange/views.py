from django.shortcuts import render
import requests
# Create your views here.

api_key = 'K9JpvHXL5LdOakeDzTxR1SOxfoWSft61'

def index(request):
    currencies = requests.get('https://api.apilayer.com/exchangerates_data/symbols', headers={'apikey': api_key}).json()
    print(currencies)
    return render(request, 'paginas/index.html', {'currencies':currencies})

def page2(request):
    de = request.GET.get('from')
    para = request.GET.get('to')
    quantidade = request.GET.get('amount')
    
    response = requests.get(f'https://api.apilayer.com/exchangerates_data/convert?to={de}&from={para}&amount={quantidade}', headers={'apikey': api_key}).json()
    
    return render(request, 'paginas/page2.html', {'response':response})