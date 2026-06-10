from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import redirect
from .models import Shoes, TagPost, Category
from .forms import AddPostForm
import os
import uuid

from django.conf import settings


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

def handle_uploaded_file(f):

    ext = os.path.splitext(f.name)[1]

    unique_name = f"{uuid.uuid4().hex}{ext}"

    file_path = os.path.join(
        settings.MEDIA_ROOT,
        'uploads',
        unique_name
    )

    os.makedirs(
        os.path.dirname(file_path),
        exist_ok=True
    )

    with open(file_path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

    return f"uploads/{unique_name}"

from .forms import UploadFileForm

def upload_file(request):

    if request.method == 'POST':

        form = UploadFileForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():
            handle_uploaded_file(
                request.FILES['file']
            )

    else:
        form = UploadFileForm()

    return render(
        request,
        'shoes/upload.html',
        {'form': form}
    )

from .forms import AddPostModelForm
from .utils import DataMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

class AddPage(CreateView):
    form_class = AddPostModelForm
    template_name = 'shoes/addpage_model.html'
    success_url = reverse_lazy('home')

    extra_context = {
        'menu': menu,
        'title': 'Добавление обуви'
    }

def addpage(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)

        print("VALID =", form.is_valid())
        print("ERRORS =", form.errors)

        if form.is_valid():
            print(form.cleaned_data)

    else:
        form = AddPostForm()

    return render(
        request,
        'shoes/addpage.html',
        {'form': form}
    )

def contact(request):
    return HttpResponse("Обратная связь")

def login(request):
    return HttpResponse("Авторизация")

from django.views.generic import ListView

class HomePage(DataMixin, ListView):
    template_name = 'shoes/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Shoes.published.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return self.get_mixin_context(
            context,
            title='Главная страница: Покупка кроссовок'
        )

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

from django.views.generic import DetailView

class ShowPost(DetailView):
    model = Shoes
    template_name = 'shoes/post.html'
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = context['post']
        context['menu'] = menu
        context['cat_selected'] = 1

        return context

class TagPostList(ListView):
    template_name = 'shoes/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Shoes.published.filter(
            tags__slug=self.kwargs['tag_slug']
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        tag = TagPost.objects.get(
            slug=self.kwargs['tag_slug']
        )

        context['title'] = f'Тег: {tag.tag}'
        context['menu'] = menu
        context['cat_selected'] = None

        return context

class ShowCategory(ListView):
    template_name = 'shoes/index.html'
    context_object_name = 'posts'
    allow_empty = False
    paginate_by = 3

    def get_queryset(self):
        return Shoes.published.filter(
            cat__slug=self.kwargs['cat_slug']
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        category = get_object_or_404(
            Category,
            slug=self.kwargs['cat_slug']
        )

        context['title'] = f'Рубрика: {category.name}'
        context['cat_selected'] = category.pk
        context['menu'] = menu

        return context

from django.views.generic.edit import UpdateView

class UpdatePage(UpdateView):
    model = Shoes

    fields = [
        'title',
        'content',
        'photo',
        'slug',
        'cat'
    ]

    template_name = 'shoes/addpage_model.html'

    success_url = reverse_lazy('home')

    extra_context = {
        'menu': menu,
        'title': 'Редактирование товара'
    }

from django.views.generic.edit import DeleteView

class DeletePage(DeleteView):
    model = Shoes

    template_name = 'shoes/delete_confirm.html'

    success_url = reverse_lazy('home')