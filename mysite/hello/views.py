from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.urls import reverse
from django.views import generic



def counter(request):
    visits = request.session.get('count', 0)
    request.session['count'] = visits % 5 + 1
    output = f'view count={request.session["count"]}'
    response = HttpResponse(output)
    response.set_cookie('dj4e_cookie', '974c7c43', max_age=1000)
    return response




def owner(request):
       return HttpResponse("Hello, world. 89332a47 is the polls index.")
