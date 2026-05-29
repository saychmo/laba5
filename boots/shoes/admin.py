from django.contrib import admin
from .models import Shoes, Category


@admin.register(Shoes)
class ShoesAdmin(admin.ModelAdmin):
    list_display = ('title', 'time_create', 'is_published', 'cat', 'brief_info')
    list_display_links = ('title', )
    ordering = ['time_create', 'title', ]
    list_editable = ('is_published', )
    list_per_page = 5
    search_fields = ['title', 'cat__name']
    list_filter = ['cat__name', 'is_published']
    actions = ['set_published', 'set_draft']
    fields = [
        'title',
        'slug',
        'content',
        'barcode',
        'tags'
    ]
    prepopulated_fields = {
        "slug": ("title",)
    }
    filter_horizontal = ['tags']
    @admin.display(description="Краткое описание")  
    def brief_info(self, shoes: Shoes):
        return f"Описание {len(shoes.content)} символов."
    @admin.action(description="Опубликовать выбранные записи")
    def set_published(self, request, queryset):
        count = queryset.update(is_published=True)
        self.message_user(
            request,
            f"Опубликовано записей: {count}"
        )
    @admin.action(description="Снять с публикации")
    def set_draft(self, request, queryset):
        count = queryset.update(is_published=False)
        self.message_user(
            request,
            f"Снято с публикации записей: {count}"
        )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')