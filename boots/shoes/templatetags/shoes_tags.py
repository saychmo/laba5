from django import template
from ..models import Category, TagPost
import shoes.views as views
from django.db.models import Count


register = template.Library()

@register.simple_tag()
def get_categories():
    return views.cats_db

@register.inclusion_tag('shoes/list_categories.html')
def show_categories(cat_selected_id=0):
    cats = Category.objects.annotate(total=Count("posts")).filter(total__gt=0)
    return {"cats": cats, "cat_selected": cat_selected_id}

@register.inclusion_tag('shoes/list_tags.html')
def show_all_tags():
    return {"tags": TagPost.objects.all()}