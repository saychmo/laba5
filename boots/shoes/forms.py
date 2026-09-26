from django import forms
from django.core.exceptions import ValidationError

from .models import Shoes, Comment


class AddPostModelForm(forms.ModelForm):

    class Meta:
        model = Shoes
        fields = [
            'title',
            'slug',
            'content',
            'photo',
            'is_published',
            'cat',
            'barcode',
            'tags'
        ]

    def clean_title(self):
        title = self.cleaned_data['title']

        if len(title) > 15:
            raise forms.ValidationError(
                'Длина названия превышает 15 символов'
            )

        return title


def russian_validator(value):
    allowed = (
        "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯ"
        "абвгдеёжзийклмнопрстуфхцчшщьыъэюя"
        "0123456789- "
    )

    if not set(value) <= set(allowed):
        raise ValidationError(
            "Только русские буквы"
        )


class AddPostForm(forms.Form):
    title = forms.CharField(
        max_length=255,
        min_length=5,
        validators=[russian_validator],
        label="Заголовок",
        error_messages={
            'required': 'Поле обязательно для заполнения.',
            'min_length': (
                'Минимальная длина названия составляет 5 символов.'
            ),
            'max_length': (
                'Максимальная длина названия составляет 255 символов.'
            )
        }
    )

    slug = forms.SlugField(
        max_length=255,
        label="URL"
    )

    content = forms.CharField(
        widget=forms.Textarea(),
        required=False,
        label="Текст"
    )


class UploadFileForm(forms.Form):
    file = forms.FileField(
        label="Файл"
    )


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['text']
        labels = {
            'text': 'Комментарий'
        }
        widgets = {
            'text': forms.Textarea(
                attrs={
                    'rows': 4,
                    'placeholder': 'Введите комментарий...'
                }
            )
        }