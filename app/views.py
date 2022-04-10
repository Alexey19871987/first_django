import datetime
import os
from django.http import HttpResponse
from django.shortcuts import render


def list_file(request):
    path = '.'
    list_f = []
    rez = sorted(os.listdir(path))
    for n, item in enumerate(rez):
        list_f.append(f'{n} - {item} ')
    return HttpResponse(list_f)


def current_time(request):
    return HttpResponse(datetime.datetime.now())


def list_func(request):
    return HttpResponse(f'/{current_time.__name__}/,'
                        f'/{list_file.__name__}/')
