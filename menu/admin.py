from django.contrib import admin
from django.contrib.auth.models import User, Group

from menu.models import Menu, MenuElement


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    autocomplete_fields = ('main_menu_element',)


class ChildrenInline(admin.TabularInline):
    model = MenuElement
    extra = 0
    show_change_link = True


@admin.register(MenuElement)
class MenuElementAdmin(admin.ModelAdmin):
    search_fields = ('text',)
    autocomplete_fields = ('parent',)
    inlines = (ChildrenInline,)


admin.site.unregister(User)
admin.site.unregister(Group)
