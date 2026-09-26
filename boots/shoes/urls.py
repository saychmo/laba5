from django.urls import path

from . import views


urlpatterns = [
    path(
        '',
        views.HomePage.as_view(),
        name='home'
    ),

    path(
        'about/',
        views.AboutPage.as_view(),
        name='about'
    ),

    path(
        'add/',
        views.AddPage.as_view(),
        name='add_page'
    ),

    path(
        'add-form/',
        views.addpage,
        name='add_form'
    ),

    path(
        'contact/',
        views.contact,
        name='contact'
    ),

    path(
        'post/<slug:post_slug>/',
        views.ShowPost.as_view(),
        name='post'
    ),

    path(
        'category/<slug:cat_slug>/',
        views.ShowCategory.as_view(),
        name='category'
    ),

    path(
        'tag/<slug:tag_slug>/',
        views.TagPostList.as_view(),
        name='tag'
    ),

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

    path(
        'post/<int:shoe_id>/comment/',
        views.AddCommentView.as_view(),
        name='add_comment'
    ),

    path(
        'post/<int:shoe_id>/like/',
        views.LikeView.as_view(),
        name='like'
    ),

    path(
        'upload/',
        views.upload_file,
        name='upload'
    ),
]