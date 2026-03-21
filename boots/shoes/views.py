from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import redirect


class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b

menu = [{'title': "О сайте", 'url_name': 'about'}, 
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
    ]

cats_db = [
    {'id': 1, 'name': 'Актрисы'},
    {'id': 2, 'name': 'Певицы'},
    {'id': 3, 'name': 'Спортсменки'},
]

data_db = [
    {'id': 1, 'title': 'Nike', 'content': '''<h1>Nike</h1> Компания, 
     основанная 25 января 1964 года под названием Blue Ribbon Sports, 
     официально стала Nike, Inc. в 1978 году[7][8]. Nike продаёт свою продукцию
      под собственным брендом, а также под марками Nike Golf, Nike Pro, Nike +, 
     Air Jordan, Nike Blazers, Air Force 1, Nike Dunk, Air Max, Foamposite, Nike Skateboarding, 
     Nike CR7, Hurley International, Converse[9]. Nike является спонсором многих спортсменов и 
     спортивных команд по всему миру.''', 'is_published': True},
    {'id': 2, 'title': 'Adidas', 'content': 'Описание бренда adidas', 'is_published': False},
    {'id': 3, 'title': 'Puma', 'content': 'Описание бренда puma', 'is_published': True},
]

def addpage(request):
    return HttpResponse("Добавление статьи")

def contact(request):
    return HttpResponse("Обратная связь")

def login(request):
    return HttpResponse("Авторизация")

def index(request):
    data = {
        'title': 'Главная страница: Покупка кроссовок',
        'menu': menu,
        'posts': data_db,
    }

    return render(request, 'shoes/index.html', context=data)


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

def about(request):
    return render(request, 'shoes/about.html', {'title': 'О сайте', 'menu': menu})

def show_post(request, post_id):
    return HttpResponse(f"Отображение статьи с id = {post_id}")
