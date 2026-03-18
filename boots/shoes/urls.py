from django.urls import path, re_path, register_converter
from shoes import views
from shoes import converters


register_converter(converters.FourDigitYearConverter,
"year4")
register_converter(converters.ShoeSizeConverter, 'size')

urlpatterns = [
    path('', views.index),
    path('cats/<int:cat_id>/', views.categories),
    path('archive/<year4:year>/', views.archive),
    path('size/<size:shoe_size>/', views.by_size),
    #re_path(r'^archive/(?P<year>[0-9]{4})/', views.archive),
    path('cats/<slug:cat_slug>/', views.categories_by_slug),
    path('size30/', views.size30, name='size30'),
]

