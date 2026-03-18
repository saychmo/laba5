from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import redirect


def index(request):
    return HttpResponse("Сайт для покупки кроссовок")

def categories(request, cat_id):
    if cat_id > 50:
        return HttpResponseRedirect('/')
    if cat_id < 30:
        return redirect('size30')
    return HttpResponse(f"<h1>Кроссовки по размеру:</h1><p >id: {cat_id}</p>")

def categories_by_slug(request, cat_slug):
    if request.POST:
        print(request.POST)
    return HttpResponse(f"<h1>Статьи по категориям</h1>slug: {cat_slug}</p>")

def archive(request, year):
    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")

def by_size(request, shoe_size):
    return HttpResponse(f"Показана обувь {shoe_size} размера")

def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

def size30(request):
    return HttpResponse("<h1>На этом сайты обувь только для взрослых</h1>")