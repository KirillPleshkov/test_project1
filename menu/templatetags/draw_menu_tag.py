from django import template

from menu.services import MenuHierarchyService

register = template.Library()


@register.inclusion_tag('menu/draw_menu.html')
def draw_menu(menu_name, selected_menu_element_slug):
    menu_hierarchy_service = MenuHierarchyService(menu_name, selected_menu_element_slug)
    menu_elements = menu_hierarchy_service.get_menu_hierarchy()
    return {
        'menu_elements': [menu_elements],
        'menu_name': menu_name,
        'selected_element': menu_hierarchy_service.selected_menu_element
    }
