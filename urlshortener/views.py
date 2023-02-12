from django.shortcuts import render, redirect
import random
from .models import Url
import string

# Create your views here.
def index(request):
    base_url = 'http://127.0.0.1:8000/'
    d_url = None

    if request.method == 'POST':
        url = request.POST['url']
        if url != None and url !='':
            slug = ''.join([random.choice(string.ascii_letters) for i in range(10)])
            
            Url.objects.create(url=url, slug=slug)
            d_url = f'{base_url}{slug}'
            print('Did it')

    return render(request, 'index.html', {'url': d_url})


def visit_url(request, slug):

    short_url = Url.objects.get(slug=slug)
    return render(request, 'urls.html', {'url':short_url.url})

def clearDb(request):
    items = Url.objects.all()
    for item in item:
        item.delete()
