from django.shortcuts import render
from django.http import HttpResponse
from intermidiate.url_shortener import shortener
from django.shortcuts import render, redirect
from .models import Url

# Create your views here.




def index(request):
    return render(request, 'index.html')

def shorten(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        short_id = shortener()
        Url.objects.create(url=url, short_id=short_id)
        short_url = request.build_absolute_uri('/') + short_id
        return render(request, 'shorten.html', {'short_url': short_url})
    else:
        return redirect('index')

def redirect_to_url(request, short_id):
    url = Url.objects.filter(short_id=short_id).first()
    if url:
        return redirect(url.url)
    else:
        return HttpResponse(f'No URL found for {short_id}')
