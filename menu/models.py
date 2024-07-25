from django.db import models


class Menu(models.Model):
    """Сущность описывающая меню"""
    name = models.CharField(max_length=100, verbose_name='название', unique=True)
    main_menu_element = models.ForeignKey(
        'MenuElement',
        on_delete=models.CASCADE,
        verbose_name='основной элемент меню'
    )

    class Meta:
        verbose_name = 'меню'
        verbose_name_plural = 'меню'

    def __str__(self):
        return self.name


class MenuElement(models.Model):
    """Сущность описывающая элементы меню"""
    text = models.CharField(max_length=100, verbose_name='текст', unique=True)
    slug = models.SlugField(max_length=100, verbose_name='slug', unique=True)
    parent_menu = models.ForeignKey(
        Menu,
        on_delete=models.CASCADE,
        related_name='elements',
        verbose_name='меню'
    )
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='children',
        verbose_name='родитель'
    )

    class Meta:
        verbose_name = 'элемент меню'
        verbose_name_plural = 'элементы меню'

    def __str__(self):
        return self.text
