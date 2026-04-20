from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import redirect
from .models import Shoes


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
    {'id': 1, 'name': 'Кроссовки'},
    {'id': 2, 'name': 'Кеды'},
    {'id': 3, 'name': 'Ботинки'},
]



def addpage(request):
    return HttpResponse("Добавление статьи")

def contact(request):
    return HttpResponse("Обратная связь")

def login(request):
    return HttpResponse("Авторизация")

def index(request):
    posts = Shoes.published.all()
    data = {
        'title': 'Главная страница: Покупка кроссовок',
        'menu': menu,
        'posts': posts,
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

def show_post(request, post_slug):
    post = get_object_or_404(Shoes, slug=post_slug)
    data = {
        'title': post.title,
        'menu': menu,
        'post': post,
        'cat_selected': 1,
    }
    return render(request, 'shoes/post.html', context=data)