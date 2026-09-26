from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class PublishedModel(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(
            is_published=Shoes.Status.PUBLISHED
        )


class Shoes(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'

    title = models.CharField(
        max_length=255,
        verbose_name="Название обуви"
    )

    slug = models.SlugField(
        max_length=255,
        db_index=True,
        unique=True,
        verbose_name="Slug"
    )

    content = models.TextField(
        blank=True,
        verbose_name="Описание"
    )

    time_create = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Время создания"
    )

    time_update = models.DateTimeField(
        auto_now=True,
        verbose_name="Время обновления"
    )

    is_published = models.BooleanField(
        choices=Status.choices,
        default=Status.DRAFT,
        verbose_name="Статус публикации"
    )

    cat = models.ForeignKey(
        'Category',
        on_delete=models.PROTECT,
        related_name='posts',
        verbose_name="Категория"
    )

    tags = models.ManyToManyField(
        'TagPost',
        blank=True,
        related_name='tags',
        verbose_name="Теги"
    )

    barcode = models.OneToOneField(
        'Barcode',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='shoes',
        verbose_name="Штрихкод"
    )

    photo = models.ImageField(
        upload_to='photos/%Y/%m/%d/',
        blank=True,
        null=True,
        verbose_name='Фото'
    )

    # Пользователь, создавший обувь
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='shoes',
        verbose_name='Автор'
    )

    objects = models.Manager()
    published = PublishedModel()

    class Meta:
        verbose_name = 'Best shoes'
        verbose_name_plural = 'Best shoes'
        ordering = ['-time_create']
        permissions = [
            (
                'discount_access',
                'Can use discount access'
            ),
        ]
        indexes = [
            models.Index(fields=['-time_create']),
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    def likes_count(self):
        return self.likes.count()


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        db_index=True,
        verbose_name="Категория"
    )

    slug = models.SlugField(
        max_length=255,
        unique=True,
        db_index=True
    )

    def get_absolute_url(self):
        return reverse(
            'category',
            kwargs={'cat_slug': self.slug}
        )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class TagPost(models.Model):
    tag = models.CharField(
        max_length=100,
        db_index=True
    )

    slug = models.SlugField(
        max_length=255,
        unique=True,
        db_index=True
    )

    def get_absolute_url(self):
        return reverse(
            'tag',
            kwargs={'tag_slug': self.slug}
        )

    def __str__(self):
        return self.tag


class Barcode(models.Model):
    name = models.CharField(
        max_length=100
    )

    serial_number = models.CharField(
        max_length=50,
        unique=True
    )

    manufacturing_date = models.DateField()

    country_of_origin = models.CharField(
        max_length=100
    )

    def __str__(self):
        return self.name


class Comment(models.Model):
    shoe = models.ForeignKey(
        Shoes,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Обувь'
    )

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор',
    )

    text = models.TextField(
        verbose_name='Комментарий'
    )

    time_create = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Время создания'
    )

    class Meta:
        ordering = ['-time_create']
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f'Комментарий {self.author.username} к "{self.shoe.title}"'


class Like(models.Model):
    shoe = models.ForeignKey(
        Shoes,
        on_delete=models.CASCADE,
        related_name='likes',
        verbose_name='Обувь'
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='likes',
        verbose_name='Пользователь'
    )

    time_create = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Время создания'
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['shoe', 'user'],
                name='unique_shoe_user_like'
            )
        ]
        verbose_name = 'Лайк'
        verbose_name_plural = 'Лайки'

    def __str__(self):
        return f'{self.user.username} → {self.shoe.title}'