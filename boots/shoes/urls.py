from django.urls import path, re_path, register_converter
from shoes import views
from shoes import converters


register_converter(converters.FourDigitYearConverter,
"year4")
register_converter(converters.ShoeSizeConverter, 'size')

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('addpage/', views.addpage, name='add_page'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('post/<slug:post_slug>/', views.ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', views.ShowCategory.as_view(), name='category'),
    path('tag/<slug:tag_slug>/', views.TagPostList.as_view(), name='tag'),
    path('addpage-model/', views.AddPage.as_view(), name='addpage_model'),
    path('upload/', views.upload_file, name='upload'),
    path(
        'edit/<int:pk>/',
        views.UpdatePage.as_view(),
        name='edit_page'
    ),

    path(
        'delete/<int:pk>/',
        views.DeletePage.as_view(),
        name='delete_page'
    ),
]