from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    context = {
        'user': request.user
    }
    return render(request, 'demo/index.html', context)

@login_required
def secure(request):
    return HttpResponse('Secure page. <a href="/openid/logout">Logout</a>')
